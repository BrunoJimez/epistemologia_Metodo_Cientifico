#!/usr/bin/env python3
"""Valida âncoras internas e registra verificação HTTP concorrente."""
from __future__ import annotations
import re
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
html_path = ROOT / "output" / "html" / "da-mente-ao-metodo-cientifico.html"
text = html_path.read_text(encoding="utf-8")
ids = set(re.findall(r'\bid="([^"]+)"', text))
internal = re.findall(r'href="#([^"]+)"', text)
missing = sorted(set(internal) - ids)
urls = sorted(set(re.findall(r'href="(https?://[^"]+)"', text)))

def check(url):
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 CodexBookAudit/1.0"}, method="HEAD")
    try:
        with urllib.request.urlopen(request, timeout=12) as response:
            return url, response.status, "ok"
    except urllib.error.HTTPError as exc:
        if exc.code in (403, 405, 429):
            return url, exc.code, "acesso restrito; destino respondeu"
        return url, exc.code, "erro HTTP"
    except Exception as exc:
        return url, "—", f"não verificado: {type(exc).__name__}"

results = []
with ThreadPoolExecutor(max_workers=12) as pool:
    futures = [pool.submit(check, url) for url in urls]
    for future in as_completed(futures):
        results.append(future.result())
results.sort()

lines = [
    "# Relatório de links",
    "",
    f"- Links internos: {len(internal)}",
    f"- Âncoras internas ausentes: {missing or 'nenhuma'}",
    f"- URLs externas únicas: {len(urls)}",
    "",
    "| URL | status | observação |",
    "|---|---:|---|",
]
for url, status, note in results:
    lines.append(f"| {url} | {status} | {note} |")
(ROOT / "references" / "relatorio-links.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
if missing:
    raise SystemExit(f"Links internos sem destino: {missing}")
print(f"Links internos válidos; {len(urls)} URLs externas registradas.")
