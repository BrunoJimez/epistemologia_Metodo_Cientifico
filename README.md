# Da mente ao método científico

Projeto editorial reprodutível do livro de Bruno Oliveira Costa Jimez, com data de corte em 20 de agosto de 2026.

## Entregáveis prontos

- `manuscript/livro.md`: manuscrito integral em Markdown.
- `output/html/da-mente-ao-metodo-cientifico.html`: HTML autônomo, acessível e com citações clicáveis.
- `output/pdf/da-mente-ao-metodo-cientifico.pdf`: PDF A4 final.
- `output/epub/da-mente-ao-metodo-cientifico.epub`: EPUB 3.
- `references/`: levantamento, matriz editorial, bibliografias e auditorias.
- `assets/diagrams/`: seis diagramas SVG, com descrição textual.
- `experiments/plano-inclinado/`: protocolo, fichas, dados simulados e análise reprodutível.

## Reproduzir

No PowerShell, a partir desta pasta:

```powershell
python scripts/build.py
python scripts/audit_citations.py
python scripts/validate_links.py
python experiments/plano-inclinado/analise.py
```

O script `build.py` usa Python, Markdown e WeasyPrint. Ele recompõe `manuscript/livro.md`, HTML, PDF e EPUB a partir dos arquivos-fonte. Não altera os volumes I-IV originais na pasta-mãe.

## Convenções editoriais

- Dados didáticos inventados aparecem sempre como **DADOS SIMULADOS**.
- Afirmações históricas específicas usam referências numéricas clicáveis.
- “Primeiro preservado” nunca significa “inventor absoluto”.
- Prova matemática, adequação empírica e precisão estatística permanecem separadas.
- Os SVGs contêm `title`, `desc` e texto alternativo equivalente em `assets/diagrams/LEIA-ME.md`.

## Licença e direitos

Texto original preparado para o autor. Fontes externas são citadas; não foram reproduzidos trechos extensos protegidos. O leitor deve verificar os direitos antes de redistribuir edições que incorporem materiais de terceiros.
