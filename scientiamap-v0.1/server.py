#!/usr/bin/env python3
"""ScientiaMap local server: static app + federated scholarly metadata search.

Only Python's standard library is used. Sources: Crossref, Europe PMC and arXiv.
No API key or paid service is required. The server does not download paywalled text.
"""
from __future__ import annotations

import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import webbrowser
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
USER_AGENT = "ScientiaMap/0.1 (open research tool; contact: local-user)"


def fetch_json(url: str, timeout: int = 18) -> dict[str, Any]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def fetch_text(url: str, timeout: int = 18) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/atom+xml"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8")


def first_year(item: dict[str, Any]) -> int | None:
    for key in ("published-print", "published-online", "issued", "created"):
        parts = item.get(key, {}).get("date-parts", [])
        if parts and parts[0] and isinstance(parts[0][0], int):
            return parts[0][0]
    return None


def crossref(query: str, year_from: str, year_to: str) -> list[dict[str, Any]]:
    filters = []
    if year_from:
        filters.append(f"from-pub-date:{year_from}-01-01")
    if year_to:
        filters.append(f"until-pub-date:{year_to}-12-31")
    params = {"query.bibliographic": query, "rows": "12", "select": "DOI,title,author,published-print,published-online,issued,created,container-title,type,URL,license"}
    if filters:
        params["filter"] = ",".join(filters)
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode(params)
    items = fetch_json(url).get("message", {}).get("items", [])
    results = []
    for rank, item in enumerate(items):
        authors = []
        for author in item.get("author", [])[:12]:
            name = " ".join(part for part in (author.get("given", ""), author.get("family", "")) if part).strip()
            if name:
                authors.append(name)
        title = " ".join(item.get("title") or []).strip()
        if not title:
            continue
        results.append({
            "id": f"crossref:{item.get('DOI') or title}", "title": title, "authors": authors,
            "year": first_year(item), "venue": " ".join(item.get("container-title") or []),
            "doi": item.get("DOI"), "url": item.get("URL"), "source": "Crossref",
            "type": item.get("type"), "openAccess": bool(item.get("license")), "_rank": rank,
        })
    return results


def europe_pmc(query: str, year_from: str, year_to: str) -> list[dict[str, Any]]:
    q = query
    if year_from or year_to:
        q += f" AND FIRST_PDATE:[{year_from or '1000'}-01-01 TO {year_to or '3000'}-12-31]"
    params = {"query": q, "format": "json", "pageSize": "12", "resultType": "core"}
    data = fetch_json("https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode(params))
    results = []
    for rank, item in enumerate(data.get("resultList", {}).get("result", [])):
        title = re.sub(r"<[^>]+>", "", item.get("title", "")).strip()
        if not title:
            continue
        doi = item.get("doi")
        pmcid = item.get("pmcid")
        pmid = item.get("pmid")
        url = f"https://europepmc.org/article/MED/{pmid}" if pmid else (f"https://europepmc.org/article/PMC/{pmcid}" if pmcid else (f"https://doi.org/{doi}" if doi else ""))
        authors = [part.strip() for part in item.get("authorString", "").rstrip(".").split(",") if part.strip()]
        results.append({
            "id": f"epmc:{pmcid or pmid or doi or title}", "title": title, "authors": authors,
            "year": int(item["pubYear"]) if str(item.get("pubYear", "")).isdigit() else None,
            "venue": item.get("journalTitle", ""), "doi": doi, "url": url, "source": "Europe PMC",
            "type": item.get("pubType", ""), "openAccess": item.get("isOpenAccess") == "Y", "_rank": rank,
        })
    return results


def arxiv(query: str, year_from: str, year_to: str) -> list[dict[str, Any]]:
    params = {"search_query": f"all:{query}", "start": "0", "max_results": "10", "sortBy": "relevance"}
    xml = fetch_text("https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params))
    ns = {"a": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(xml)
    results = []
    for rank, entry in enumerate(root.findall("a:entry", ns)):
        published = entry.findtext("a:published", "", ns)
        year = int(published[:4]) if published[:4].isdigit() else None
        if year_from and year and year < int(year_from):
            continue
        if year_to and year and year > int(year_to):
            continue
        title = " ".join(entry.findtext("a:title", "", ns).split())
        if not title:
            continue
        authors = [node.findtext("a:name", "", ns) for node in entry.findall("a:author", ns)]
        url = entry.findtext("a:id", "", ns)
        arxiv_id = url.rsplit("/", 1)[-1]
        results.append({
            "id": f"arxiv:{arxiv_id}", "title": title, "authors": authors, "year": year,
            "venue": "arXiv", "doi": None, "url": url, "source": "arXiv", "type": "preprint", "openAccess": True, "_rank": rank,
        })
    return results


def normalize_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", title.casefold())[:180]


def federated_search(query: str, year_from: str, year_to: str) -> tuple[list[dict[str, Any]], list[str]]:
    sources = {"Crossref": crossref, "Europe PMC": europe_pmc, "arXiv": arxiv}
    gathered: list[dict[str, Any]] = []
    errors: list[str] = []
    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = {pool.submit(fn, query, year_from, year_to): name for name, fn in sources.items()}
        for future in as_completed(futures):
            name = futures[future]
            try:
                gathered.extend(future.result())
            except Exception as exc:  # source failure must not take down the federation
                errors.append(f"{name}: {type(exc).__name__}")
    deduped: dict[str, dict[str, Any]] = {}
    for item in gathered:
        key = (item.get("doi") or "").casefold() or normalize_title(item.get("title", ""))
        if not key:
            continue
        existing = deduped.get(key)
        if existing:
            existing["source"] = " + ".join(sorted(set(existing["source"].split(" + ") + item["source"].split(" + "))))
            existing["openAccess"] = bool(existing.get("openAccess") or item.get("openAccess"))
            if not existing.get("url"):
                existing["url"] = item.get("url")
            existing["_rank"] = min(existing.get("_rank", 99), item.get("_rank", 99))
        else:
            deduped[key] = item
    results = list(deduped.values())
    results.sort(key=lambda item: (item.get("_rank", 99), -(item.get("year") or 0), item.get("title", "")))
    for item in results:
        item.pop("_rank", None)
    return results[:30], errors


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self) -> None:
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path != "/api/search":
            return super().do_GET()
        params = urllib.parse.parse_qs(parsed.query)
        query = (params.get("q") or [""])[0].strip()[:300]
        year_from = (params.get("from") or [""])[0]
        year_to = (params.get("to") or [""])[0]
        if len(query) < 2 or (year_from and not re.fullmatch(r"\d{4}", year_from)) or (year_to and not re.fullmatch(r"\d{4}", year_to)):
            return self.send_json(400, {"error": "invalid query"})
        started = time.monotonic()
        results, errors = federated_search(query, year_from, year_to)
        self.send_json(200, {"query": query, "results": results, "sourceErrors": errors, "elapsedMs": round((time.monotonic() - started) * 1000)})

    def send_json(self, status: int, payload: dict[str, Any]) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt: str, *args: Any) -> None:
        print(f"[ScientiaMap] {self.address_string()} - {fmt % args}")


def main() -> None:
    host, port = "127.0.0.1", 8765
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    server = ThreadingHTTPServer((host, port), Handler)
    url = f"http://{host}:{port}/"
    print(f"ScientiaMap disponível em {url}")
    print("Pressione Ctrl+C para encerrar.")
    try:
        webbrowser.open(url)
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nScientiaMap encerrado.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
