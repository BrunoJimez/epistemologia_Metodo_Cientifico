#!/usr/bin/env python3
"""Monta Markdown, HTML autônomo, PDF A4 e EPUB 3."""
from __future__ import annotations

import base64
import html
import io
import re
import shutil
import subprocess
import sys
import time
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT.parent
CHAPTERS = ROOT / "manuscript" / "capitulos"
REFS = ROOT / "references"
OUT_HTML = ROOT / "output" / "html" / "da-mente-ao-metodo-cientifico.html"
OUT_PDF = ROOT / "output" / "pdf" / "da-mente-ao-metodo-cientifico.pdf"
OUT_EPUB = ROOT / "output" / "epub" / "da-mente-ao-metodo-cientifico.epub"
BOOK_MD = ROOT / "manuscript" / "livro.md"


def inline_html_to_markdown(fragment: str) -> str:
    fragment = re.sub(r'<a href="#">.*?</a>', '', fragment, flags=re.S)
    fragment = re.sub(
        r'<a href="([^"]+)">(.*?)</a>',
        lambda m: f"[{re.sub(r'<[^>]+>', '', m.group(2)).strip()}]({m.group(1)})",
        fragment,
        flags=re.S,
    )
    fragment = re.sub(r'<em>(.*?)</em>', r'*\1*', fragment, flags=re.S)
    fragment = re.sub(r'<strong>(.*?)</strong>', r'**\1**', fragment, flags=re.S)
    fragment = re.sub(r'<br\s*/?>', ' ', fragment)
    fragment = re.sub(r'<[^>]+>', '', fragment)
    return re.sub(r'\s+', ' ', html.unescape(fragment)).strip()


def extract_legacy_references() -> str:
    source = SOURCE_ROOT / "volume-4-da-mente-ao-metodo-cientifico.html"
    raw = source.read_text(encoding="utf-8")
    # Correções verificadas em 20/08/2026 sem alterar o material-base do usuário.
    raw = raw.replace(
        'https://doi.org/10.1017/S0959774320000175',
        'https://doi.org/10.1017/S0959774320000165',
    )
    raw = raw.replace(
        '<a href="https://archive.org/details/rhindmathematica0000unse">Internet\nArchive</a>',
        '<a href="https://openlibrary.org/books/OL22228866M/The_Rhind_mathematical_papyrus">Open Library</a>',
    )
    raw = raw.replace(
        'https://press.uchicago.edu/ucp/books/book/chicago/S/bo4104507.html',
        'https://press.uchicago.edu/ucp/books/book/chicago/S/bo4094708.html',
    )
    raw = raw.replace(
        '<a href="https://archive.org/details/sourcebookinmedi0000unse">Internet\nArchive</a>',
        '<a href="https://search.worldcat.org/title/A-source-book-in-medieval-science/oclc/1501424063">WorldCat</a>',
    )
    found = re.findall(
        r'<p><span id="ref-(\d+)">\[\d+\]</span>(.*?)</p>', raw, flags=re.S
    )
    refs = {}
    for number, body in found:
        n = int(number)
        if n <= 80:
            refs[n] = f'<span id="ref-{n}">[{n}]</span> ' + inline_html_to_markdown(body)
    if set(refs) != set(range(1, 81)):
        missing = sorted(set(range(1, 81)) - set(refs))
        raise RuntimeError(f"Referências legadas ausentes: {missing}")
    return "\n\n".join(refs[n] for n in range(1, 81))


def build_references() -> str:
    legacy = extract_legacy_references()
    additional = (REFS / "referencias-adicionais.md").read_text(encoding="utf-8").strip()
    content = legacy + "\n\n" + additional + "\n"
    (REFS / "referencias.md").write_text("# Referências completas\n\n" + content, encoding="utf-8")
    return content


def assemble_markdown(references: str) -> str:
    pieces = []
    for path in sorted(CHAPTERS.glob("*.md")):
        text = path.read_text(encoding="utf-8").strip()
        text = text.replace("../../assets/", "../assets/")
        pieces.append(text)
    book = "\n\n".join(pieces)
    book = book.replace("# Parte I —", "[TOC]\n\n# Parte I —", 1)
    book += "\n\n# Referências\n\n" + references
    book += "\n\n# Bibliografia comentada por nível\n\n"
    commented = (REFS / "bibliografia-comentada.md").read_text(encoding="utf-8")
    commented = re.sub(r'^# Bibliografia comentada por nível\s*', '', commented)
    book += commented.strip() + "\n"
    BOOK_MD.write_text(book, encoding="utf-8")
    return book


CSS = r"""
:root { --ink:#172033; --blue:#173f6b; --teal:#0f766e; --orange:#c2410c; --paper:#fffdfa; --soft:#eef4f8; }
* { box-sizing:border-box; }
html { scroll-behavior:smooth; }
body { margin:0 auto; max-width:920px; padding:48px 62px 80px; color:var(--ink); background:var(--paper); font:18px/1.62 Georgia, 'Times New Roman', serif; text-rendering:optimizeLegibility; }
h1,h2,h3,h4 { font-family:'Segoe UI', Arial, sans-serif; color:var(--blue); line-height:1.18; page-break-after:avoid; break-after:avoid-page; }
h1 { font-size:2.45rem; margin:2.4em 0 .7em; border-bottom:4px solid var(--teal); padding-bottom:.22em; }
h1:first-of-type { margin-top:.3em; font-size:3.1rem; border:0; text-align:center; padding-top:25vh; page-break-after:avoid; }
h2 { font-size:1.75rem; margin-top:2.1em; }
h3 { font-size:1.28rem; margin-top:1.7em; }
p { margin:.75em 0; orphans:3; widows:3; }
a { color:#0b5a8e; text-decoration-thickness:.06em; text-underline-offset:.14em; }
blockquote { border-left:5px solid var(--orange); background:#fff4e8; padding:.7em 1.15em; margin:1.2em 0; }
code { font-family:'Cascadia Mono', Consolas, monospace; background:#edf2f7; padding:.08em .3em; border-radius:3px; font-size:.9em; }
table { border-collapse:collapse; width:100%; margin:1.2em 0; font-size:.89em; break-inside:auto; }
thead { display:table-header-group; }
tr { break-inside:avoid; }
th { background:#dbe9f2; color:#102a43; text-align:left; }
th,td { border:1px solid #9fb3c4; padding:.48em .58em; vertical-align:top; }
img { display:block; max-width:100%; max-height:700px; margin:1.4em auto; break-inside:avoid; }
nav.toc, .toc { background:var(--soft); border:1px solid #b7c9d6; padding:1.2em 1.5em; margin:2em 0; page-break-before:auto; }
.toc::before { content:'Sumário'; display:block; font:700 1.8rem 'Segoe UI',Arial,sans-serif; color:var(--blue); margin-bottom:.6em; }
.toc ul { list-style:none; padding-left:1em; }
.toc > ul { padding-left:0; }
.toc a { text-decoration:none; }
hr { border:0; border-top:1px solid #9fb3c4; }
@media (max-width:700px) { body{padding:24px 18px;font-size:16px} h1:first-of-type{padding-top:10vh;font-size:2.3rem} table{display:block;overflow-x:auto} }
@media print {
  body { max-width:none; padding:0; background:white; font-size:10.35pt; line-height:1.46; }
  h1 { font-size:23pt; page-break-before:auto; string-set: section content(); }
  h1:first-of-type { page-break-before:auto; padding-top:62mm; font-size:32pt; }
  h1[id^="parte-"], h1#apêndices, h1#referências, h1#bibliografia-comentada-por-nível { page-break-before:always; }
  h2 { font-size:16pt; string-set: chapter content(); }
  h3 { font-size:12.5pt; }
  a { color:inherit; text-decoration:none; }
  nav.toc, .toc { font-size:9.4pt; }
  img { max-height:175mm; }
}
@page { size:A4; margin:18mm 17mm 20mm 21mm; @bottom-center{content:counter(page);font:9pt 'Segoe UI';color:#52606d} @top-center{content:string(chapter);font:8pt 'Segoe UI';color:#52606d} }
@page:first { @top-center{content:none} @bottom-center{content:none} }
"""


def render_markdown(book: str) -> str:
    try:
        import markdown
    except ImportError as exc:
        raise RuntimeError("Instale o pacote Python 'markdown' para montar o livro") from exc
    # YAML é preservado no Markdown, mas removido do corpo renderizado.
    book_for_html = re.sub(r'^---\n.*?\n---\n', '', book, count=1, flags=re.S)
    return markdown.markdown(
        book_for_html,
        extensions=["extra", "toc", "sane_lists"],
        extension_configs={"toc": {"permalink": False, "toc_depth": "1-3"}},
    )


def embed_svg_images(rendered: str) -> str:
    def repl(match):
        alt, src = match.group(1), match.group(2)
        name = Path(src).name
        candidate = ROOT / "assets" / "diagrams" / name
        if not candidate.exists():
            return match.group(0)
        payload = base64.b64encode(candidate.read_bytes()).decode("ascii")
        return f'<img src="data:image/svg+xml;base64,{payload}" alt="{html.escape(alt, quote=True)}" />'
    return re.sub(r'<img alt="([^"]*)" src="([^"]+\.svg)"\s*/?>', repl, rendered)


def html_document(body: str) -> str:
    return f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="author" content="Bruno Oliveira Costa Jimez"><meta name="date" content="2026-08-20">
<title>Da mente ao método científico</title><style>{CSS}</style></head>
<body><main id="conteudo">{body}</main></body></html>'''


def build_epub(body: str):
    OUT_EPUB.parent.mkdir(parents=True, exist_ok=True)
    container = '<?xml version="1.0"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="EPUB/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>'
    xhtml = f'<?xml version="1.0" encoding="utf-8"?><html xmlns="http://www.w3.org/1999/xhtml" lang="pt-BR"><head><title>Da mente ao método científico</title><style>{CSS}</style></head><body>{body}</body></html>'
    nav = '<?xml version="1.0" encoding="utf-8"?><html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="pt-BR"><head><title>Sumário</title></head><body><nav epub:type="toc"><ol><li><a href="text.xhtml">Da mente ao método científico</a></li></ol></nav></body></html>'
    opf = '''<?xml version="1.0" encoding="utf-8"?><package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid"><metadata xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:identifier id="bookid">urn:uuid:da-mente-ao-metodo-2026</dc:identifier><dc:title>Da mente ao método científico</dc:title><dc:creator>Bruno Oliveira Costa Jimez</dc:creator><dc:language>pt-BR</dc:language><dc:date>2026-08-20</dc:date><meta property="dcterms:modified">2026-08-20T00:00:00Z</meta></metadata><manifest><item id="text" href="text.xhtml" media-type="application/xhtml+xml"/><item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/></manifest><spine><itemref idref="text"/></spine></package>'''
    with zipfile.ZipFile(OUT_EPUB, "w") as z:
        z.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml", container)
        z.writestr("EPUB/content.opf", opf)
        z.writestr("EPUB/nav.xhtml", nav)
        z.writestr("EPUB/text.xhtml", xhtml)


def build_pdf(document: str):
    OUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    printable = document.replace("—", "-").replace("–", "-").replace("‑", "-")
    try:
        from weasyprint import HTML
        # Exigência editorial do fluxo PDF: hifens ASCII na versão paginada.
        HTML(string=printable, base_url=str(ROOT)).write_pdf(str(OUT_PDF))
    except ImportError:
        temp = ROOT / "tmp" / "pdfs" / "print.html"
        temp.write_text(printable, encoding="utf-8")
        candidates = [
            Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
            Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
            Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
        ]
        browser = next((p for p in candidates if p.exists()), None)
        if browser:
            profile = ROOT / "tmp" / "pdfs" / "browser-profile"
            profile.mkdir(parents=True, exist_ok=True)
            OUT_PDF.unlink(missing_ok=True)
            subprocess.run([
                str(browser), "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                f"--user-data-dir={profile}", f"--print-to-pdf={OUT_PDF}", temp.as_uri()
            ], check=True, timeout=120)
            # Edge pode devolver o controle antes do fechamento do PDF; espere o
            # tamanho permanecer estável por dois segundos para não numerar um
            # arquivo apenas parcialmente escrito.
            last_size, stable = -1, 0
            for _ in range(150):
                size = OUT_PDF.stat().st_size if OUT_PDF.exists() else 0
                if size > 1000 and size == last_size:
                    stable += 1
                else:
                    stable = 0
                last_size = size
                if stable >= 10:
                    break
                time.sleep(0.2)
            if not OUT_PDF.exists() or stable < 10:
                raise RuntimeError("O navegador não produziu o PDF esperado")
            add_page_furniture(OUT_PDF)
            return
        executable = shutil.which("weasyprint")
        if not executable:
            raise RuntimeError("Nenhum renderizador PDF disponível")
        subprocess.run([executable, str(temp), str(OUT_PDF)], check=True)


def add_page_furniture(pdf_path: Path):
    """Sobrepõe cabeçalho discreto e numeração após impressão do navegador."""
    from pypdf import PdfReader, PdfWriter
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfgen import canvas

    arial = Path(r"C:\Windows\Fonts\arial.ttf")
    furniture_font = "Helvetica"
    if arial.exists():
        pdfmetrics.registerFont(TTFont("ArialEmbedded", str(arial)))
        furniture_font = "ArialEmbedded"
    reader = PdfReader(str(pdf_path))
    writer = PdfWriter()
    total = len(reader.pages)
    for index, page in enumerate(reader.pages, start=1):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        packet = io.BytesIO()
        c = canvas.Canvas(packet, pagesize=(width, height))
        c.setFillColorRGB(0.32, 0.38, 0.43)
        c.setFont(furniture_font, 8)
        if index > 1:
            c.drawCentredString(width / 2, height - 18, "Da mente ao método científico")
            c.drawCentredString(width / 2, 15, f"{index} / {total}")
        c.save()
        packet.seek(0)
        overlay = PdfReader(packet).pages[0]
        page.merge_page(overlay)
        writer.add_page(page)
    temp_path = pdf_path.with_suffix(".numbered.pdf")
    with temp_path.open("wb") as handle:
        writer.write(handle)
    temp_path.replace(pdf_path)


def main():
    references = build_references()
    book = assemble_markdown(references)
    rendered = embed_svg_images(render_markdown(book))
    document = html_document(rendered)
    OUT_HTML.parent.mkdir(parents=True, exist_ok=True)
    OUT_HTML.write_text(document, encoding="utf-8")
    build_epub(rendered)
    build_pdf(document)
    print(f"Markdown: {BOOK_MD}")
    print(f"HTML: {OUT_HTML}")
    print(f"PDF: {OUT_PDF}")
    print(f"EPUB: {OUT_EPUB}")


if __name__ == "__main__":
    main()
