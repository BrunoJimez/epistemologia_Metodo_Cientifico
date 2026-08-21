# ScientiaMap beta 0.1

Protótipo funcional e portátil de um laboratório metodológico aberto. Ele transforma uma dúvida em um projeto organizado em 12 etapas, decompõe o texto de um artigo no mesmo framework, exibe um mapa iterativo e busca metadados científicos sem API paga.

## Como abrir

### Windows

1. Extraia todo o ZIP.
2. Dê dois cliques em `iniciar-windows.bat`.
3. O navegador abrirá em `http://127.0.0.1:8765/`.
4. Para encerrar, feche a janela preta ou pressione `Ctrl+C` nela.

Requisito: Python 3. O programa não instala pacotes e não requer chave de API.

### Linux ou macOS

No terminal, dentro da pasta:

```sh
chmod +x iniciar-linux-macos.sh
./iniciar-linux-macos.sh
```

Também é possível abrir `index.html` diretamente para usar os módulos locais. A busca bibliográfica exige iniciar `server.py`.

## O que já funciona

- interface em português brasileiro, inglês, espanhol e chinês simplificado (`zh-CN`);
- construtor de estudo com 12 etapas, critérios transparentes, bloqueio progressivo e retorno;
- avanço excepcional com justificativa registrada;
- persistência no navegador (`localStorage`);
- análise heurística de artigos colados ou carregados em TXT, Markdown, HTML, CSV, TeX e JSON;
- mapa metodológico clicável;
- pesquisa federada em Crossref, Europe PMC e arXiv;
- desduplicação por DOI ou título;
- exportação para Markdown, HTML, Word compatível (`.doc`), CSV compatível com Excel, LaTeX, JSON e impressão/PDF;
- importação do projeto em JSON.

## Limites honestos desta versão

- “Pronta” significa que a documentação mínima da etapa foi preenchida. Não certifica verdade, validade, ética ou qualidade estatística.
- A classificação de artigos é heurística e exibe correspondência textual, não avaliação por pares nem risco de viés.
- PDF, DOCX e XLSX precisam ser convertidos em texto para análise nesta versão. A arquitetura completa prevê Docling/GROBID e Pandoc.
- Nenhuma base indexa toda a ciência. A busca retorna até 30 resultados e depende da disponibilidade e política de cada fonte.
- Não há contorno de paywalls. O aplicativo aponta apenas metadados e conteúdo indicado como aberto.
- Dados do projeto ficam no navegador do dispositivo. Faça exportações JSON regulares.

## Licenciamento proposto

- aplicativo: GNU AGPL-3.0-or-later;
- rubricas, traduções e documentação: CC BY-SA 4.0;
- conteúdo inserido pelo pesquisador: permanece sob controle do pesquisador.

Leia `scientiamap-especificacao-v0.1.pdf` no pacote externo para arquitetura, modelo de dados, fontes, riscos e roteiro de produção.
