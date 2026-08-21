#!/usr/bin/env python3
"""Renderiza todas as páginas e cria folhas de contato para inspeção visual."""
from __future__ import annotations
import math
from pathlib import Path
import fitz
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
pdf = ROOT / "output" / "pdf" / "da-mente-ao-metodo-cientifico.pdf"
out = ROOT / "tmp" / "pdfs" / "rendered"
out.mkdir(parents=True, exist_ok=True)
doc = fitz.open(pdf)
thumbs = []
for index, page in enumerate(doc, 1):
    pix = page.get_pixmap(matrix=fitz.Matrix(1.35, 1.35), alpha=False)
    path = out / f"page-{index:03d}.png"
    pix.save(path)
    image = Image.open(path).convert("RGB")
    image.thumbnail((245, 345))
    thumbs.append((index, image.copy()))

cols, rows = 4, 4
cell_w, cell_h = 270, 385
for sheet_index in range(math.ceil(len(thumbs) / (cols * rows))):
    sheet = Image.new("RGB", (cols * cell_w, rows * cell_h), "#d9e2ec")
    draw = ImageDraw.Draw(sheet)
    subset = thumbs[sheet_index * cols * rows:(sheet_index + 1) * cols * rows]
    for j, (page_no, thumb) in enumerate(subset):
        x = (j % cols) * cell_w + (cell_w - thumb.width) // 2
        y = (j // cols) * cell_h + 25
        sheet.paste(thumb, (x, y))
        draw.text((j % cols * cell_w + 12, j // cols * cell_h + 5), f"p. {page_no}", fill="#102a43")
    sheet.save(out / f"contact-{sheet_index + 1:02d}.png")
print(f"Renderizadas {len(doc)} páginas em {out}")
