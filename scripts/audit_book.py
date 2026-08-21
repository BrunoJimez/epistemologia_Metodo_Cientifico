#!/usr/bin/env python3
"""Validação estrutural dos entregáveis finais."""
from __future__ import annotations
import re
import zipfile
from pathlib import Path
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
book_path = ROOT / "manuscript" / "livro.md"
html_path = ROOT / "output" / "html" / "da-mente-ao-metodo-cientifico.html"
pdf_path = ROOT / "output" / "pdf" / "da-mente-ao-metodo-cientifico.pdf"
epub_path = ROOT / "output" / "epub" / "da-mente-ao-metodo-cientifico.epub"

required = [
    book_path, html_path, pdf_path, epub_path,
    ROOT / "references" / "referencias.md",
    ROOT / "references" / "claims.csv",
    ROOT / "experiments" / "plano-inclinado" / "dados-simulados.csv",
    ROOT / "experiments" / "plano-inclinado" / "resultado-analise.json",
]
missing_files = [str(p.relative_to(ROOT)) for p in required if not p.exists()]

book = book_path.read_text(encoding="utf-8")
body_without_refs = book.split("\n# Referências\n", 1)[0]
words = re.findall(r"\b[\wÀ-ÿ]+(?:[-’'][\wÀ-ÿ]+)*\b", body_without_refs)
chapters = [int(x) for x in re.findall(r'^## (\d+)\.', body_without_refs, flags=re.M)]
chapter_ok = chapters == list(range(1, 31))
required_terms = [
    "x + 3 = 5", "F = ma", "s(t) = s₀ + v₀t + ½at²", "equação do calor",
    "Maxwell", "Grossmann", "Hilbert", "DADOS SIMULADOS", "Lean", "resíduos",
]
missing_terms = [x for x in required_terms if x not in book]

html_text = html_path.read_text(encoding="utf-8")
img_tags = re.findall(r'<img\b[^>]*>', html_text)
missing_alt = [tag[:120] for tag in img_tags if not re.search(r'\balt="[^"]+"', tag)]
html_lang = 'lang="pt-BR"' in html_text

reader = PdfReader(str(pdf_path))
page_count = len(reader.pages)
page_sizes = {(round(float(p.mediabox.width), 1), round(float(p.mediabox.height), 1)) for p in reader.pages}
empty_pages = []
replacement_chars = []
font_status: dict[str, bool] = {}

def descriptor_embeds_font(descriptor) -> bool:
    if descriptor is None:
        return False
    descriptor = descriptor.get_object()
    return any(key in descriptor for key in ("/FontFile", "/FontFile2", "/FontFile3"))

def register_font(font_ref) -> None:
    font = font_ref.get_object()
    name = str(font.get("/BaseFont", font.get("/Name", "fonte-sem-nome")))
    subtype = str(font.get("/Subtype", ""))
    embedded = subtype == "/Type3" or descriptor_embeds_font(font.get("/FontDescriptor"))
    for descendant_ref in font.get("/DescendantFonts", []):
        descendant = descendant_ref.get_object()
        descendant_name = str(descendant.get("/BaseFont", name))
        descendant_embedded = descriptor_embeds_font(descendant.get("/FontDescriptor"))
        font_status[descendant_name] = font_status.get(descendant_name, False) or descendant_embedded
        embedded = embedded or descendant_embedded
    font_status[name] = font_status.get(name, False) or embedded

for index, page in enumerate(reader.pages, 1):
    text = page.extract_text() or ""
    if len(text.strip()) < 5:
        empty_pages.append(index)
    if "�" in text:
        replacement_chars.append(index)
    resources_ref = page.get("/Resources")
    if resources_ref:
        resources = resources_ref.get_object()
        fonts_ref = resources.get("/Font")
        if fonts_ref:
            for font_ref in fonts_ref.get_object().values():
                register_font(font_ref)

base14_names = {
    "/Courier", "/Courier-Bold", "/Courier-Oblique", "/Courier-BoldOblique",
    "/Helvetica", "/Helvetica-Bold", "/Helvetica-Oblique", "/Helvetica-BoldOblique",
    "/Times-Roman", "/Times-Bold", "/Times-Italic", "/Times-BoldItalic",
    "/Symbol", "/ZapfDingbats",
}
unembedded_fonts = sorted(name for name, embedded in font_status.items() if not embedded and name not in base14_names)

with zipfile.ZipFile(epub_path) as z:
    bad_zip = z.testzip()
    names = set(z.namelist())
    epub_required = {"mimetype", "META-INF/container.xml", "EPUB/content.opf", "EPUB/nav.xhtml", "EPUB/text.xhtml"}
    epub_missing = sorted(epub_required - names)
    mimetype_ok = z.read("mimetype") == b"application/epub+zip"

links_report = (ROOT / "references" / "relatorio-links.md").read_text(encoding="utf-8") if (ROOT / "references" / "relatorio-links.md").exists() else ""
hard_link_errors = re.findall(r'\| (404|500|501|502|503) \|', links_report)

failures = []
if missing_files: failures.append(f"arquivos ausentes: {missing_files}")
if not chapter_ok: failures.append(f"sequência de capítulos: {chapters}")
if missing_terms: failures.append(f"termos obrigatórios ausentes: {missing_terms}")
if missing_alt or not html_lang: failures.append("acessibilidade HTML")
if page_count < 20 or len(page_sizes) != 1: failures.append("paginação PDF")
if replacement_chars: failures.append(f"glifos de substituição no PDF: {replacement_chars}")
if unembedded_fonts: failures.append(f"fontes não incorporadas no PDF: {unembedded_fonts}")
if bad_zip or epub_missing or not mimetype_ok: failures.append("estrutura EPUB")
if hard_link_errors: failures.append(f"links HTTP com erro confirmado: {hard_link_errors}")

report = [
    "# Relatório final de auditoria técnica",
    "",
    f"- Palavras no corpo anterior às referências: {len(words)}",
    f"- Capítulos numerados: {len(chapters)} (sequência 1–30: {'sim' if chapter_ok else 'não'})",
    f"- PDF: {page_count} páginas; tamanhos: {sorted(page_sizes)} pontos",
    f"- Páginas sem texto extraível: {empty_pages or 'nenhuma'}",
    f"- Páginas com glifo de substituição: {replacement_chars or 'nenhuma'}",
    f"- Fontes PDF detectadas: {len(font_status)}; não incorporadas (exceto Base 14): {unembedded_fonts or 'nenhuma'}",
    f"- HTML: {len(img_tags)} imagens; sem texto alternativo: {len(missing_alt)}; idioma pt-BR: {'sim' if html_lang else 'não'}",
    f"- EPUB: ZIP íntegro: {'sim' if not bad_zip else 'não'}; mimetype: {'correto' if mimetype_ok else 'incorreto'}; ausências: {epub_missing or 'nenhuma'}",
    f"- Links externos com 404/5xx após correções: {len(hard_link_errors)}",
    f"- Dados simulados marcados: {'sim' if 'DADOS SIMULADOS' in book else 'não'}",
    f"- Resultado geral: {'APROVADO' if not failures else 'REPROVADO'}",
    "",
    "## Itens editoriais revisados",
    "",
    "- nomes Einstein, Grossmann, Hilbert, Bradwardine, Heytesbury, Swineshead, Dumbleton e Oresme;",
    "- datas centrais e distinção entre publicação on-line e versão de registro em 2026;",
    "- usos de primeiro, inventor, prova e descoberta qualificados no relatório de citações;",
    "- fórmulas acompanhadas por unidades, hipóteses e domínio nas anatomias e no apêndice;",
    "- conjunto experimental e gráfico identificados como simulados.",
]
if failures:
    report += ["", "## Falhas", ""] + [f"- {item}" for item in failures]
(ROOT / "references" / "relatorio-auditoria-final.md").write_text("\n".join(report) + "\n", encoding="utf-8")
if failures:
    raise SystemExit("; ".join(failures))
print(f"Auditoria final aprovada: {page_count} páginas, {len(words)} palavras no corpo.")
