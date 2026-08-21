#!/usr/bin/env python3
"""Audita citações, âncoras, linguagem de prioridade e dados simulados."""
from __future__ import annotations
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
book = (ROOT / "manuscript" / "livro.md").read_text(encoding="utf-8")
cites = [int(x) for x in re.findall(r'\(#ref-(\d+)\)', book)]
defs = [int(x) for x in re.findall(r'<span id="ref-(\d+)">', book)]
undefined = sorted(set(cites) - set(defs))
unused = sorted(set(defs) - set(cites))
duplicates = sorted(k for k, v in Counter(defs).items() if v != 1)

risky = {}
for term in ["primeiro", "inventor", "inventou", "provou", "prova", "descoberta"]:
    risky[term] = len(re.findall(rf'\b{term}\w*\b', book, flags=re.I))

csv_sim = (ROOT / "experiments" / "plano-inclinado" / "dados-simulados.csv").read_text(encoding="utf-8")
sim_rows = [line for line in csv_sim.splitlines()[1:] if line.strip()]
unmarked_sim = [i + 2 for i, line in enumerate(sim_rows) if not line.startswith("DADOS SIMULADOS,")]

report = [
    "# Relatório de auditoria de citações e linguagem",
    "",
    f"- Ocorrências de citações: {len(cites)}",
    f"- Referências citadas: {len(set(cites))}",
    f"- Referências definidas: {len(set(defs))}",
    f"- Citações sem definição: {undefined or 'nenhuma'}",
    f"- Referências definidas e não citadas: {unused or 'nenhuma'}",
    f"- Definições duplicadas: {duplicates or 'nenhuma'}",
    f"- Linhas simuladas sem marca: {unmarked_sim or 'nenhuma'}",
    "",
    "## Termos de risco revisados",
    "",
]
report.extend(f"- `{k}`: {v} ocorrências" for k, v in risky.items())
report += [
    "",
    "As ocorrências não são erros automáticos. Foram mantidas quando qualificadas por critério (por exemplo, 'primeiro preservado') ou usadas para negar uma concepção equivocada.",
]
(ROOT / "references" / "relatorio-auditoria-citacoes.md").write_text("\n".join(report) + "\n", encoding="utf-8")

if undefined or unused or duplicates or unmarked_sim:
    raise SystemExit("Auditoria falhou; consulte references/relatorio-auditoria-citacoes.md")
print("Auditoria de citações concluída sem falhas.")
