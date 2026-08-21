#!/usr/bin/env python3
"""Analisa exclusivamente o conjunto marcado como DADOS SIMULADOS."""
from __future__ import annotations

import csv
import json
import math
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "dados-simulados.csv"


def fit_two_parameter(x, y):
    n = len(x)
    xm, ym = statistics.fmean(x), statistics.fmean(y)
    sxx = sum((v - xm) ** 2 for v in x)
    if sxx == 0:
        raise ValueError("Preditor sem variação")
    slope = sum((a - xm) * (b - ym) for a, b in zip(x, y)) / sxx
    intercept = ym - slope * xm
    residuals = [b - (intercept + slope * a) for a, b in zip(x, y)]
    rmse = math.sqrt(sum(r * r for r in residuals) / n)
    return intercept, slope, residuals, rmse


def svg_plot(rows, quad):
    width, height = 1000, 620
    left, right, top, bottom = 100, 50, 70, 90
    xs = [r["tempo_s"] ** 2 for r in rows]
    ys = [r["posicao_m"] for r in rows]
    xmax, ymax = max(xs) * 1.06, max(ys) * 1.08

    def px(x):
        return left + x / xmax * (width - left - right)

    def py(y):
        return height - bottom - y / ymax * (height - top - bottom)

    b0, b1 = quad[0], quad[1]
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img">',
        '<title>Posição contra tempo ao quadrado — dados simulados</title>',
        '<desc>Pontos simulados e regressão quadrática linearizada para o plano inclinado.</desc>',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        f'<line x1="{left}" y1="{height-bottom}" x2="{width-right}" y2="{height-bottom}" stroke="#172554" stroke-width="3"/>',
        f'<line x1="{left}" y1="{top}" x2="{left}" y2="{height-bottom}" stroke="#172554" stroke-width="3"/>',
        '<text x="500" y="35" text-anchor="middle" font-family="Arial" font-size="26" font-weight="700">PLANO INCLINADO — DADOS SIMULADOS</text>',
        f'<text x="500" y="{height-25}" text-anchor="middle" font-family="Arial" font-size="22">t² (s²)</text>',
        f'<text x="28" y="300" text-anchor="middle" transform="rotate(-90 28 300)" font-family="Arial" font-size="22">posição s (m)</text>',
        f'<line x1="{px(0)}" y1="{py(b0)}" x2="{px(xmax)}" y2="{py(b0+b1*xmax)}" stroke="#ea580c" stroke-width="5"/>',
    ]
    for r in rows:
        parts.append(f'<circle cx="{px(r["tempo_s"]**2):.2f}" cy="{py(r["posicao_m"]):.2f}" r="5" fill="#2563eb" opacity="0.72"/>')
    parts.append(f'<text x="{left+20}" y="{top+35}" font-family="Arial" font-size="18">s = {b0:.4f} + {b1:.4f} t²</text>')
    parts.append('</svg>')
    (ROOT / "grafico-plano-inclinado.svg").write_text("\n".join(parts), encoding="utf-8")


with SOURCE.open(encoding="utf-8", newline="") as handle:
    raw = list(csv.DictReader(handle))

if not raw or any(r["status"] != "DADOS SIMULADOS" for r in raw):
    raise RuntimeError("O script exige que todas as linhas sejam marcadas DADOS SIMULADOS")

rows = [
    {**r, "posicao_m": float(r["posicao_m"]), "tempo_s": float(r["tempo_s"])}
    for r in raw
    if r["excluida"].lower() != "true"
]

summary = []
for position in sorted({r["posicao_m"] for r in rows}):
    values = [r["tempo_s"] for r in rows if r["posicao_m"] == position]
    summary.append({
        "status": "DADOS SIMULADOS",
        "posicao_m": position,
        "n": len(values),
        "tempo_medio_s": statistics.fmean(values),
        "desvio_padrao_s": statistics.stdev(values),
    })

t = [r["tempo_s"] for r in rows]
s = [r["posicao_m"] for r in rows]
linear = fit_two_parameter(t, s)
quadratic = fit_two_parameter([v * v for v in t], s)

result = {
    "status": "DADOS SIMULADOS",
    "arquivo": SOURCE.name,
    "n": len(rows),
    "modelo_linear": {"intercepto_m": linear[0], "coef_m_s": linear[1], "rmse_m": linear[3]},
    "modelo_quadratico": {"intercepto_m": quadratic[0], "coef_m_s2": quadratic[1], "aceleracao_estimada_m_s2": 2 * quadratic[1], "rmse_m": quadratic[3]},
    "interpretacao": "Comparação didática; não constitui medição real ou histórica.",
}

(ROOT / "resultado-analise.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

with (ROOT / "resumo-por-posicao.csv").open("w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=summary[0].keys())
    writer.writeheader(); writer.writerows(summary)

with (ROOT / "residuos.csv").open("w", encoding="utf-8", newline="") as handle:
    fields = ["status", "run_id", "tempo_s", "posicao_m", "residuo_linear_m", "residuo_quadratico_m"]
    writer = csv.DictWriter(handle, fieldnames=fields); writer.writeheader()
    for row, rl, rq in zip(rows, linear[2], quadratic[2]):
        writer.writerow({"status": "DADOS SIMULADOS", "run_id": row["run_id"], "tempo_s": row["tempo_s"], "posicao_m": row["posicao_m"], "residuo_linear_m": rl, "residuo_quadratico_m": rq})

svg_plot(rows, quadratic)
print(json.dumps(result, ensure_ascii=False, indent=2))
