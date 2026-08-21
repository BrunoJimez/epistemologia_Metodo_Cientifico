---
title: "ScientiaMap"
subtitle: "Especificação científica, funcional e arquitetural — beta 0.1"
author: "Documento de concepção e protótipo"
date: "13 de agosto de 2026"
lang: pt-BR
toc: true
toc-depth: 3
numbersections: false
link-citations: true
colorlinks: true
geometry: margin=2.4cm
fontsize: 11pt
---

# Resumo executivo

O **ScientiaMap** é uma proposta de infraestrutura pública para ensinar, planejar, registrar, analisar e comunicar investigações científicas. Sua unidade fundamental não é o “texto gerado por inteligência artificial”, mas a ligação auditável entre **pergunta, afirmação, evidência, decisão, incerteza e fonte**. O protótipo beta 0.1 acompanha o pesquisador por 12 etapas iterativas, analisa o conteúdo textual de artigos no mesmo framework, oferece um mapa metodológico e pesquisa metadados em Crossref, Europe PMC e arXiv sem API paga.

O sistema nasce de uma correção epistemológica decisiva: preencher um formulário não torna uma afirmação verdadeira. Ciência não é uma escada universal e irreversível, mas uma família de práticas que alterna construção conceitual, representação formal, observação, intervenção, inferência e crítica pública. Reprodutibilidade e replicação são meios de escrutínio, não selos automáticos de verdade; a confiança científica se constrói pelo conjunto de evidências e críticas acumuladas.[1](#ref-1)

A versão completa deve ser **livre, multilíngue, local por padrão, federada e extensível**. Seu núcleo determinístico precisa funcionar sem modelos generativos. Modelos locais podem auxiliar na classificação e na redação, mas nunca criar evidência ausente, ocultar incerteza ou decidir sozinhos que um estudo está “correto”.

## Resultado entregue na beta 0.1

| Módulo | O que já funciona | Limite explícito |
|---|---|---|
| Construir estudo | 12 etapas, portas de prontidão, retorno, ressalva justificada, salvamento local | Prontidão documental não certifica validade |
| Analisar artigo | Entrada textual; localização de trechos; estágio, cobertura e confiança heurística | Não é revisão por pares nem ferramenta de risco de viés |
| Mapa metodológico | Visão das 12 etapas e estado do projeto | O diagrama é uma orientação geral, não um método único |
| Buscar literatura | Crossref, Europe PMC e arXiv; filtros anuais; desduplicação | Não representa toda a literatura e depende das fontes |
| Importar/exportar | JSON, Markdown, HTML, Word compatível, CSV/Excel, LaTeX e PDF por impressão | Conversão fiel de fórmulas e layouts complexos virá depois |
| Idiomas | Português brasileiro, inglês, espanhol e chinês simplificado | Tradução metodológica precisa de revisão comunitária contínua |

# 1. Problema e visão

Ferramentas acadêmicas normalmente começam tarde demais: ajudam a formatar referências, redigir um manuscrito ou executar uma análise depois que decisões fundamentais já foram tomadas. O ScientiaMap começa antes, no momento em que alguém diz: **“observei isto; por que acontece?”**. Ele preserva a genealogia dessa dúvida até as conclusões e a crítica pública.

O objetivo não é impor um ritual único. Ensaios randomizados, pesquisas observacionais, provas matemáticas, estudos qualitativos, simulações, revisões sistemáticas e física teórica têm estruturas distintas. Diretrizes de relato reconhecem essa diversidade: CONSORT trata ensaios randomizados; STROBE, estudos observacionais; PRISMA, revisões sistemáticas; EQUATOR cataloga diretrizes para muitos outros desenhos.[2](#ref-2) [3](#ref-3) [4](#ref-4) [5](#ref-5) O framework de 12 etapas é, portanto, um **vocabulário de tradução entre desenhos**, não um substituto das normas específicas.

## 1.1 Princípios inegociáveis

1. **Evidência antes de eloquência.** O sistema deve distinguir texto persuasivo de material probatório.
2. **Proveniência por padrão.** Toda afirmação, transformação, decisão e arquivo relevante deve ter origem e histórico.
3. **Incerteza visível.** Resultados sem intervalo, erro, alternativas ou limitações não recebem aparência de certeza.
4. **Iteração registrada.** Voltar a uma etapa é comportamento científico normal; o retorno deve gerar histórico, não punição.
5. **Pluralismo metodológico.** Regras variam conforme desenho, área, população, risco e pergunta.
6. **Local primeiro.** Conteúdo de pesquisa permanece no dispositivo por padrão.
7. **Federação, não monopólio.** A descoberta combina fontes; nenhuma base é tratada como “toda a ciência”.
8. **Acessibilidade e internacionalização.** A meta de interface é WCAG 2.2 nível AA.[6](#ref-6)
9. **Software e documentação livres.** Código, rubricas e traduções devem permitir auditoria e reutilização.
10. **Autoridade humana responsável.** Automação recomenda; pesquisadores, orientadores, especialistas, comunidades e comitês decidem.

## 1.2 Não objetivos

O ScientiaMap não deve:

- declarar uma hipótese “provada” por ter passado pelas etapas;
- conceder aprovação ética, clínica, jurídica ou de biossegurança;
- substituir estatísticos, metodologistas, bibliotecários, revisores ou orientadores;
- avaliar a verdade de uma teoria apenas por consistência matemática;
- contornar paywalls ou redistribuir texto sem licença;
- inventar referências, dados, números de página, trechos ou resultados ausentes;
- calcular uma nota opaca de “qualidade científica”;
- esconder divergências metodológicas atrás de uma resposta única.

# 2. Modelo epistemológico operacional

## 2.1 A unidade de raciocínio

Cada projeto deve ser representado por um grafo de objetos:

| Objeto | Pergunta que responde | Exemplo |
|---|---|---|
| Observação | O que foi registrado? | “A dissolução parece mais rápida na água quente.” |
| Pergunta | O que queremos saber? | “Como a temperatura altera o tempo de dissolução?” |
| Afirmação | O que está sendo alegado? | “Maior temperatura reduz o tempo médio.” |
| Hipótese | Qual resposta provisória será confrontada? | Relação negativa entre temperatura e tempo |
| Conceito | O que os termos significam? | “Dissolvido” = ausência de cristais visíveis após agitação padronizada |
| Modelo | Que estrutura simplificada relaciona entidades? | Taxa dependente da temperatura sob massa e agitação constantes |
| Predição | O que deve ocorrer se o modelo for adequado? | Mediana de tempo menor a 60 °C do que a 20 °C |
| Evidência | Que registro sustenta ou contraria uma afirmação? | Tabela de tempos com calibração e metadados |
| Decisão | Que escolha foi feita e por quê? | Excluir teste interrompido por queda do recipiente |
| Incerteza | O que permanece indeterminado? | Erro do termômetro e variabilidade de agitação |
| Fonte | De onde veio o material? | DOI, página, parágrafo, arquivo, autor, data |

Dados e fluxos devem seguir princípios de encontrabilidade, acessibilidade, interoperabilidade e reutilização — FAIR — sem confundir “acessível” com “necessariamente aberto”.[7](#ref-7) A proveniência pode ser modelada de forma compatível com PROV-O, que representa entidades, atividades e agentes.[8](#ref-8) Pacotes de pesquisa podem adotar RO-Crate para agrupar dados, código, pessoas e metadados em uma estrutura transportável.[9](#ref-9)

## 2.2 Três classes de validação

O produto precisa exibir sempre qual validação está sendo feita:

| Classe | Pergunta | Pode ser automatizada? | Consequência permitida |
|---|---|---|---|
| Completude | Os campos e artefatos mínimos existem? | Em grande parte | “Documentado para avançar” |
| Coerência | As partes não apresentam incompatibilidades detectáveis? | Parcialmente | “Requer revisão desta relação” |
| Validade | O desenho, a inferência e a evidência sustentam a conclusão no mundo? | Não de modo geral | “Requer julgamento especializado e crítica” |

Na beta 0.1, a porta verifica apenas **completude transparente**: tamanho mínimo dos registros e três itens declarativos. Esses limites são deliberadamente visíveis e substituíveis. Não são uma escala psicométrica validada.

## 2.3 Estados permitidos

- **Em elaboração:** material insuficiente ou ainda editado.
- **Pronta para prosseguir:** critérios documentais explícitos satisfeitos.
- **Com ressalva:** o pesquisador decidiu prosseguir e registrou a lacuna e a razão.
- **Reaberta:** uma mudança posterior exige revisão.
- **Requer especialista:** risco, conflito ou domínio ultrapassa a competência configurada.
- **Sinal crítico:** possível problema ético, legal, de segurança ou integridade; o sistema interrompe recomendações automáticas.

Não existe o estado automático “verdadeira”.

# 3. Framework de 12 etapas

## 3.1 Visão completa

| Etapa | Produto mínimo | Porta de prontidão | Retornos frequentes |
|---:|---|---|---|
| 1. Fenômeno e problema | observação delimitada; relevância; contexto | observação separada de interpretação | 4, 8, 9 |
| 2. Pergunta investigável | pergunta específica; unidade; desfecho | pode receber evidência contrária | 3, 4, 8 |
| 3. Conhecimento e hipótese | síntese inicial; rivais; hipótese provisória | fontes e rivais registradas | 2, 5, 7 |
| 4. Conceitos e operações | definições; indicadores; instrumentos | termos observáveis ou justificadamente abstratos | 2, 5, 8 |
| 5. Modelo e domínio | entidades; relações; idealizações; limites | pressupostos e domínio explícitos | 3, 4, 6 |
| 6. Representação formal | variáveis; unidades; equações ou algoritmos | símbolos definidos e consistência examinada | 4, 5, 7 |
| 7. Consequências e predições | previsões; rivais; incompatibilidade | previsões distinguíveis antecedem o teste | 3, 5, 8 |
| 8. Desenho e instrumentos | protocolo; amostra; controles; ética; análise | desenho responde à pergunta e riscos são tratados | 2, 4, 7 |
| 9. Observação e dados | dados; metadados; desvios; calibração | proveniência e qualidade preservadas | 4, 8, 10 |
| 10. Análise e incerteza | código; estimativas; erro; sensibilidade | decisões auditáveis e incerteza relatada | 5, 8, 9 |
| 11. Confronto e interpretação | comparação previsão–resultado; rivais; limites | conclusão não ultrapassa evidência | 3, 5, 10 |
| 12. Comunicação e crítica | relato; materiais; autoria; licença; replicação | terceiros podem compreender e escrutinar | qualquer etapa |

A pré-registração pode ser sugerida entre as etapas 7 e 9: ela registra o plano antes do exame dos dados e ajuda a distinguir análises confirmatórias de explorações posteriores.[10](#ref-10) O produto não deve proibir exploração; deve rotulá-la corretamente.

## 3.2 Adaptadores por desenho

O mesmo estágio assume produtos diferentes conforme o estudo:

| Desenho | Predição ou consequência | Dados ou material probatório | Análise ou confronto |
|---|---|---|---|
| Experimento controlado | diferença sob manipulação | medidas por condição e controles | efeito, incerteza, vieses e alternativas |
| Observacional | associação temporal/estrutural | coorte, caso-controle, transversal etc. | confundimento, seleção, mensuração; STROBE quando aplicável |
| Ensaio randomizado | efeito da intervenção | fluxo de participantes e desfechos | análise planejada, perdas, danos; CONSORT 2025 |
| Revisão sistemática | padrão esperado no corpo de evidência | registros identificados, excluídos e incluídos | síntese, heterogeneidade, viés; PRISMA 2020 |
| Qualitativo | expectativas sensitizantes, não necessariamente hipótese preditiva | entrevistas, observação, documentos | codificação, reflexividade, casos negativos |
| Computacional | comportamento do modelo e testes | código, parâmetros, sementes, benchmarks | verificação, validação e sensibilidade |
| Teórico/matemático | teorema, consequência lógica ou estrutura | axiomas, definições, lemas e prova | validade dedutiva; relação empírica só quando alegada |
| Física teórica | consequências formais e observacionais | matemática + dados externos/experimentos | consistência e confronto empírico são julgamentos distintos |

Essa adaptação impede um erro central: uma prova matemática estabelece uma conclusão **dentro de um sistema formal a partir de premissas**; não demonstra, por si só, que as premissas modelam adequadamente a realidade. Na ciência empírica, a matemática comprime relações e produz consequências precisas; a adequação ao mundo depende de mensuração, desenho, comparação e crítica.

# 4. Analisador de artigos

## 4.1 Pipeline de produção

1. **Ingestão:** PDF, HTML, JATS XML, DOCX, XLSX, Markdown, LaTeX ou texto.
2. **Extração:** preservar página, bloco, tabela, figura, equação e ordem de leitura.
3. **Segmentação:** dividir em unidades citáveis com identificador estável.
4. **Detecção de desenho:** estimar tipo de estudo, registrando confiança e sinais usados.
5. **Mapeamento:** associar cada unidade a uma ou mais etapas.
6. **Extração de objetos:** pergunta, afirmação, amostra, variáveis, instrumentos, equações, estimativas, incerteza, limitações e referências.
7. **Auditoria:** exibir trecho original, localização, regra/modelo e confiança.
8. **Lacunas:** dizer “não localizado” em vez de inventar.
9. **Aplicação de adaptador:** sugerir diretriz específica sem confundi-la com avaliação de mérito.
10. **Exportação:** tabela de evidências e mapa artigo–framework.

GROBID transforma publicações técnicas em TEI XML estruturado e é adequado para referências e estrutura científica.[11](#ref-11) Docling aceita múltiplos formatos e representa layout, tabelas e fórmulas em um modelo documental unificado.[12](#ref-12) Na arquitetura recomendada, Docling é o conversor geral e GROBID é um especialista para literatura científica; os resultados passam por reconciliação, não por confiança cega.

## 4.2 Resultado que a interface deve mostrar

Para cada associação:

- etapa e subitem;
- trecho exato curto;
- página, seção e parágrafo;
- tipo de evidência — declaração do autor, método relatado, resultado, limitação etc.;
- confiança da classificação;
- razão da associação;
- alerta quando só o resumo, e não o método completo, sustenta a inferência;
- botão “corrigir classificação”, cuja decisão alimenta conjunto de avaliação local.

## 4.3 O que “não localizado” significa

Ausência detectada pode significar: o artigo omitiu o item; o item está em suplemento; a extração falhou; a terminologia não foi reconhecida; o desenho não exige aquele item. Por isso, o sistema nunca converte ausência textual diretamente em “má ciência”. Diretrizes de relato ajudam a verificar transparência, mas relato e condução do estudo são dimensões relacionadas e distintas.

# 5. Construtor guiado como “jogo sério”

## 5.1 Mecânica segura

O sistema usa progressão, mas evita transformar ciência em competição por pontos. A recompensa é a **clareza do projeto**, não uma pontuação de verdade. Cada fase tem:

- missão;
- exemplo completo e contraexemplo;
- artefatos obrigatórios e opcionais;
- perguntas socráticas;
- verificação automática de completude;
- revisão humana configurável;
- decisão “pronta”, “reabrir” ou “avançar com ressalva”;
- histórico das alterações.

Fases futuras permanecem bloqueadas apenas no **modo de aprendizagem**. Em modo exploratório, o pesquisador pode navegar livremente. Mesmo no modo bloqueado, qualquer etapa anterior pode ser reaberta; etapas dependentes recebem o estado “revisão necessária”.

## 5.2 Dependências e invalidação

Se a definição operacional muda na etapa 4, o sistema deve sinalizar possíveis impactos nas etapas 5 a 11. Se uma análise não planejada é adicionada na etapa 10, ela deve ser rotulada como exploratória, sem apagar o plano original. Se o instrumento falha na etapa 9, a etapa 8 é reaberta e o desvio permanece no histórico.

Essa propagação transforma o mapa em uma ferramenta de raciocínio: não há apenas 12 caixas, mas relações causais e documentais entre decisões.

# 6. Descoberta de literatura sem API paga

## 6.1 Estratégia federada

O requisito correto não é “buscar todos os estudos”, promessa tecnicamente impossível. É buscar **múltiplas fontes declaradas, medir cobertura, respeitar políticas, deduplicar e permitir expansão**.

| Fonte | Papel | Acesso e cuidado |
|---|---|---|
| Crossref | DOI e metadados editoriais multidisciplinares | REST público; usar identificação e boas práticas do pool educado.[13](#ref-13) |
| Europe PMC | biomedicina, resumos, citações e indicadores de acesso | REST público.[14](#ref-14) |
| PubMed/NCBI | literatura biomédica | E-utilities; obedecer limites e identificação.[15](#ref-15) |
| PMC | texto completo quando a licença permite | OAI-PMH oferece metadados e somente textos com direitos de reutilização adequados.[16](#ref-16) |
| arXiv | preprints em física, matemática, computação e áreas próximas | API Atom; API legada limita a uma solicitação a cada três segundos.[17](#ref-17) |
| DOAJ | periódicos e artigos de acesso aberto | API e OAI-PMH; validar versão e campos vigentes.[18](#ref-18) |
| SciELO | forte cobertura latino-americana e multilíngue | integrar serviços e coleções oficiais; preservar coleção de origem |
| OAI-PMH | federação de repositórios institucionais | protocolo de baixo limiar com seis verbos.[19](#ref-19) |
| Unpaywall | localização legal de versões abertas por DOI | API gratuita, requer identificação por e-mail.[20](#ref-20) |
| OpenAlex | grafo de obras, autores, instituições e citações | em 2026 exige chave; há orçamento diário gratuito e snapshot aberto, mas uso ilimitado hospedado não deve ser prometido.[21](#ref-21) |

## 6.2 Processo de consulta

1. preservar a pergunta original;
2. extrair conceitos e sinônimos por idioma;
3. construir consultas separadas por fonte;
4. registrar consulta, data, filtros e versão;
5. receber metadados sem redistribuir conteúdo indevido;
6. normalizar DOI, ORCID, títulos, autores, datas e tipos;
7. deduplicar por DOI e, secundariamente, por similaridade de título/autor/ano;
8. separar preprint, versão aceita e versão de registro;
9. construir grafo de citações com origem declarada;
10. permitir triagem reproduzível, motivos de exclusão e exportação.

Buscas para revisões sistemáticas exigem estratégias próprias, múltiplas bases e relato completo. O fluxo PRISMA registra identificação, triagem, inclusão e motivos de exclusão.[4](#ref-4) A busca geral do protótipo não deve ser anunciada como revisão sistemática.

# 7. Arquitetura recomendada

## 7.1 Camadas

| Camada | Tecnologia proposta | Responsabilidade |
|---|---|---|
| Interface | PWA em TypeScript/React; Tauri opcional | quatro modos, acessibilidade, mapas, trabalho offline |
| API local | Python/FastAPI | projetos, arquivos, análise, busca e exportações |
| Domínio | pacote Python independente | regras de estágio, rubricas, objetos e proveniência |
| Documentos | Docling, GROBID, Pandoc | leitura estruturada e conversão |
| Dados locais | SQLite + FTS5 ou DuckDB | projetos, índice, cache e auditoria |
| Hospedagem comunitária | PostgreSQL + armazenamento compatível com S3 | colaboração opcional e instâncias institucionais |
| Busca | conectores federados | APIs públicas, OAI-PMH e snapshots |
| IA opcional | Ollama ou llama.cpp | classificação/assistência local, sempre rastreada |
| Exportação | Pandoc, python-docx, openpyxl, LaTeX | PDF, DOCX, XLSX, HTML, TeX e Markdown |

Pandoc converte entre Markdown, HTML, LaTeX, DOCX e muitos outros formatos, além de gerar PDF e processar citações por CSL.[22](#ref-22) Ollama expõe uma API local sem autenticação, enquanto llama.cpp prioriza inferência local em ampla variedade de hardware.[23](#ref-23) [24](#ref-24) O sistema deve funcionar sem qualquer um deles; IA é um adaptador, não o núcleo.

## 7.2 Modelo de dados mínimo

```text
ResearchProject
 ├── StageRevision[]
 │    ├── Artifact[]
 │    ├── Claim[] ── EvidenceLink[] ── Evidence[]
 │    ├── Decision[]
 │    ├── Risk[]
 │    └── Validation[]
 ├── Source[]
 ├── Contributor[]
 └── AuditEvent[]
```

Campos essenciais:

- identificador UUID estável;
- versão de esquema e versão da rubrica;
- idioma original e traduções;
- autor humano ou processo que realizou a ação;
- timestamp, justificativa e objeto anterior;
- hash de artefato;
- licença e nível de acesso;
- relação entre afirmação e evidência: sustenta, contraria, contextualiza ou é inconclusiva;
- confiança de classificação separada da força da evidência.

## 7.3 API conceitual

```text
POST   /projects
GET    /projects/{id}
POST   /projects/{id}/stages/{stage}/revisions
POST   /projects/{id}/validations
POST   /documents/ingest
POST   /documents/{id}/map
GET    /search/works
POST   /claims/{id}/evidence
GET    /projects/{id}/audit
POST   /exports
```

Cada resposta automatizada deve incluir `engine`, `engine_version`, `rubric_version`, `confidence`, `evidence_spans` e `warnings`.

# 8. Formatos e interoperabilidade

| Formato | Leitura de produção | Escrita de produção | Observação |
|---|---|---|---|
| PDF | Docling/GROBID + OCR opcional | Pandoc/LaTeX ou motor HTML | preservar página e coordenadas |
| HTML | parser semântico | template acessível | sanitizar scripts e URLs |
| DOCX | Docling/python-docx | python-docx/Pandoc | estilos e comentários exigem testes |
| XLSX | openpyxl/pandas | openpyxl | fórmulas não são apenas valores |
| Markdown | Pandoc/parser | nativo | formato canônico legível |
| LaTeX | parser/Pandoc | template TeX | preservar equações e bibliografia |
| JATS XML | parser XML | exportador futuro | formato importante para artigos |
| CSV/TSV | parser tabular | nativo | exigir codificação, delimitador e dicionário |
| JSON/JSON-LD | validação por esquema | nativo | intercâmbio e proveniência |
| BibTeX/CSL JSON | parser bibliográfico | nativo | referências estruturadas |

Conversão pode perder informação. O próprio Pandoc observa que diferenças entre modelos internos de formatos podem impedir preservação de certos atributos.[22](#ref-22) Portanto, o arquivo original, o convertido, a versão da ferramenta e os avisos devem ser preservados.

# 9. Multilinguismo e acessibilidade

O idioma não é apenas uma troca de rótulos. O projeto precisa:

- usar tags BCP 47: `pt-BR`, `en`, `es`, `zh-CN`;
- preservar o texto original e tratar tradução como uma derivação;
- manter glossário metodológico versionado;
- permitir busca por sinônimos sem substituir a consulta original;
- suportar escrita e segmentação chinesas;
- aceitar referências e nomes sem romanização forçada;
- testar navegação por teclado, leitores de tela, contraste, zoom e dispositivos móveis;
- nunca comunicar estado apenas por cor.

A tradução automática pode auxiliar, mas conceitos como *evidence*, *proof*, *trial*, *bias*, *validity* e *reliability* exigem contexto disciplinar. Revisores de cada comunidade linguística devem aprovar rubricas oficiais.

# 10. Segurança, privacidade, ética e integridade

## 10.1 Ameaças principais

| Ameaça | Controle |
|---|---|
| manuscrito confidencial enviado sem intenção | processamento local por padrão; consentimento antes de serviço remoto |
| prompt injection dentro de PDF | tratar documento como dado, não como instrução |
| referência inventada | metadado precisa ser resolvido em fonte; estado “não verificado” |
| texto malicioso em HTML | sanitização, política de conteúdo e isolamento |
| vazamento de participantes | detecção de identificadores, criptografia e política de retenção |
| conclusão superconfiante | linguagem calibrada e evidência visível |
| uso clínico indevido | bloqueio de recomendações e encaminhamento a protocolo especializado |
| viés linguístico ou regional | testes estratificados e participação comunitária |
| dependência de uma API | cache, conectores alternativos, snapshots e modo offline |

## 10.2 Integridade científica

O aplicativo deve registrar versão do protocolo, mudanças pós-dados, exclusões, múltiplas análises e materiais disponibilizados. Autoria não pode ser inferida de quantidade de texto; contribuições podem usar a taxonomia CRediT para papéis como conceituação, metodologia, software, curadoria e redação.[25](#ref-25)

Boas práticas de pesquisa reproduzível incluem dados e código que permitam rerodar análises quando direitos e ética permitem.[26](#ref-26) Isso não significa publicar dados sensíveis: abertura deve ser tão ampla quanto possível e tão restrita quanto necessário.

# 11. Avaliação do próprio ScientiaMap

O produto precisa ser estudado cientificamente antes de receber alegações de eficácia.

## 11.1 Conjuntos de avaliação

- artigos de acesso aberto, estratificados por idioma, área e desenho;
- anotações independentes por pelo menos dois especialistas;
- adjudicação de desacordos;
- exemplos negativos e casos em que a etapa não se aplica;
- documentos com tabelas, fórmulas, suplementos e OCR difícil;
- projetos iniciantes e avançados acompanhados longitudinalmente.

## 11.2 Métricas

- precisão, revocação e F1 do mapeamento de trechos;
- calibração de confiança;
- taxa de evidência inventada — meta: zero;
- concordância entre anotadores;
- cobertura e duplicatas na busca;
- tempo para detectar lacunas;
- compreensão conceitual antes/depois;
- acessibilidade por tarefa;
- taxa de retornos corretos entre etapas;
- incidência de confiança indevida induzida pela interface.

Uma pontuação alta de classificação não demonstra que o software melhora ciência. Estudos de impacto devem examinar qualidade de protocolos, transparência, aprendizagem, erros prevenidos e efeitos adversos.

# 12. Roteiro de desenvolvimento

## Fase 0 — protótipo demonstrável (entregue)

- construtor local em 12 etapas;
- bloqueio, retorno e ressalva;
- quatro idiomas;
- analisador textual heurístico;
- mapa clicável;
- Crossref + Europe PMC + arXiv;
- sete exportações e importação JSON.

**Critério de saída:** fluxos demonstráveis sem dependência paga; avisos e limites visíveis.

## Fase 1 — fundação reprodutível

- repositório público, AGPL-3.0-or-later;
- schemas JSON e migrações;
- testes unitários, integração e acessibilidade;
- aplicativo PWA e API FastAPI;
- SQLite local, auditoria e snapshots;
- importação PDF/DOCX/HTML por Docling; GROBID opcional;
- exportação DOCX/XLSX/PDF real por servidor local.

**Critério de saída:** projeto criado, fechado, reaberto e exportado sem perda semântica nos campos testados.

## Fase 2 — adaptadores metodológicos

- experimental, observacional, randomizado, sistemático, qualitativo, computacional e teórico;
- ligação a EQUATOR e checklists versionados;
- plano de análise, ética, amostragem, instrumentos e riscos;
- grafo de dependências e invalidação.

**Critério de saída:** especialistas confirmam que o sistema não força rubrica inadequada ao desenho.

## Fase 3 — analisador de artigos auditável

- extração de layout e coordenadas;
- classificação conteúdo–etapa;
- afirmações, evidências, incertezas e fontes;
- correção humana e conjunto de avaliação;
- modelos locais opcionais.

**Critério de saída:** desempenho, calibração e falhas publicados por idioma e desenho.

## Fase 4 — busca aberta e síntese

- conectores adicionais, cache, snapshots e OAI-PMH;
- histórico reprodutível de consulta;
- triagem, deduplicação de versões e grafo de citações;
- tabelas de evidência sem resumo inventado.

**Critério de saída:** cobertura e erros comparados com estratégias de referência em amostras reais.

## Fase 5 — colaboração e sustentabilidade

- instância institucional opcional;
- revisão por papéis, comentários e assinatura de decisões;
- federação entre instalações;
- governança comunitária multilíngue;
- política de vulnerabilidades e manutenção de conectores.

**Critério de saída:** comunidade independente consegue instalar, auditar, traduzir e manter uma instância.

# 13. Licença e governança propostas

- **Aplicativo e servidor:** GNU AGPL-3.0-or-later, que preserva liberdades também em versões oferecidas por rede.[27](#ref-27)
- **Rubricas, exemplos, traduções e documentação:** Creative Commons Attribution-ShareAlike 4.0.[28](#ref-28)
- **Dados inseridos:** pertencem aos titulares; nenhuma licença é presumida.
- **Metadados externos:** mantêm seus termos e proveniência.
- **Modelos locais:** cada peso conserva sua licença; “open weight” não significa automaticamente software livre.

A governança deve incluir pesquisadores de diferentes métodos, bibliotecários, estatísticos, especialistas em ética, engenheiros, educadores, tradutores, estudantes e representantes de populações afetadas. Mudanças em rubricas exigem versão, justificativa e período de comentário público.

# 14. Decisões tomadas na beta 0.1

1. **Nome provisório:** ScientiaMap.
2. **Dois núcleos principais:** construir estudo e analisar artigo.
3. **Modelo de 12 etapas:** comum, porém adaptável.
4. **Porta transparente:** completude, nunca selo científico.
5. **Retorno livre:** qualquer etapa anterior pode ser revisitada.
6. **Ressalva registrada:** avanço excepcional não apaga lacunas.
7. **Heurística local inicial:** permite demonstração sem IA nem API.
8. **Busca real federada:** três fontes sem chave paga; sem alegação de exaustividade.
9. **Quatro idiomas iniciais:** `pt-BR`, `en`, `es`, `zh-CN`.
10. **Persistência local:** conteúdo fica no navegador; JSON serve de backup.
11. **Formatos graduais:** exportações leves no navegador; conversores robustos na arquitetura de produção.
12. **Licença copyleft proposta:** evitar apropriação fechada de uma infraestrutura financiada pela comunidade.

# Conclusão

O valor do ScientiaMap não está em substituir o cientista, mas em tornar visível o que frequentemente permanece implícito: de onde veio a pergunta, como conceitos foram definidos, por que um modelo foi escolhido, que previsão antecedeu os dados, que decisão alterou a análise, qual evidência sustenta cada afirmação e onde a incerteza permanece.

O produto pode começar como um guia para iniciantes e amadurecer em infraestrutura de pesquisa. Para isso, deve resistir à tentação de parecer onisciente. Um bom sistema científico não diz apenas “prossiga”; ele mostra **o que foi documentado, o que depende de julgamento, o que pode estar errado e como outra pessoa poderá verificar**.

# Referências

#### [1] {#ref-1}

National Academies of Sciences, Engineering, and Medicine. *Reproducibility and Replicability in Science*. Washington, DC: The National Academies Press, 2019. [https://doi.org/10.17226/25303](https://doi.org/10.17226/25303).

#### [2] {#ref-2}

CONSORT Group. *CONSORT 2025 Statement*. 2025. [https://www.consort-statement.org/](https://www.consort-statement.org/).

#### [3] {#ref-3}

von Elm, E. et al. “The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) Statement.” *PLoS Medicine* 4, e296, 2007. [https://www.equator-network.org/reporting-guidelines/strobe/](https://www.equator-network.org/reporting-guidelines/strobe/).

#### [4] {#ref-4}

Page, M. J. et al. “The PRISMA 2020 statement: an updated guideline for reporting systematic reviews.” *BMJ* 372, n71, 2021. [https://doi.org/10.1136/bmj.n71](https://doi.org/10.1136/bmj.n71).

#### [5] {#ref-5}

EQUATOR Network. *Reporting Guidelines Library*. [https://www.equator-network.org/reporting-guidelines/](https://www.equator-network.org/reporting-guidelines/). Acesso em 13 ago. 2026.

#### [6] {#ref-6}

W3C. *Web Content Accessibility Guidelines (WCAG) 2.2*. W3C Recommendation, 2024. [https://www.w3.org/TR/WCAG22/](https://www.w3.org/TR/WCAG22/).

#### [7] {#ref-7}

Wilkinson, M. D. et al. “The FAIR Guiding Principles for scientific data management and stewardship.” *Scientific Data* 3, 160018, 2016. [https://doi.org/10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18).

#### [8] {#ref-8}

W3C. *PROV-O: The PROV Ontology*. W3C Recommendation, 2013. [https://www.w3.org/TR/prov-o/](https://www.w3.org/TR/prov-o/).

#### [9] {#ref-9}

RO-Crate Community. *RO-Crate 1.1 Specification*. [https://www.researchobject.org/ro-crate/1.1/](https://www.researchobject.org/ro-crate/1.1/).

#### [10] {#ref-10}

Center for Open Science. *Preregistration*. [https://www.cos.io/initiatives/prereg](https://www.cos.io/initiatives/prereg). Acesso em 13 ago. 2026.

#### [11] {#ref-11}

GROBID Project. *GROBID Documentation: Introduction*. [https://grobid.readthedocs.io/en/latest/Introduction/](https://grobid.readthedocs.io/en/latest/Introduction/). Acesso em 13 ago. 2026.

#### [12] {#ref-12}

Docling Project. *Docling Documentation*. [https://docling-project.github.io/docling/](https://docling-project.github.io/docling/). Acesso em 13 ago. 2026.

#### [13] {#ref-13}

Crossref. *REST API Documentation*. [https://www.crossref.org/documentation/retrieve-metadata/rest-api/](https://www.crossref.org/documentation/retrieve-metadata/rest-api/). Acesso em 13 ago. 2026.

#### [14] {#ref-14}

Europe PMC. *RESTful Web Service*. [https://europepmc.org/RestfulWebService](https://europepmc.org/RestfulWebService). Acesso em 13 ago. 2026.

#### [15] {#ref-15}

National Center for Biotechnology Information. *APIs — E-utilities*. [https://www.ncbi.nlm.nih.gov/home/develop/api/](https://www.ncbi.nlm.nih.gov/home/develop/api/). Acesso em 13 ago. 2026.

#### [16] {#ref-16}

PubMed Central. *PMC OAI-PMH API*. [https://pmc.ncbi.nlm.nih.gov/tools/oai/](https://pmc.ncbi.nlm.nih.gov/tools/oai/). Acesso em 13 ago. 2026.

#### [17] {#ref-17}

arXiv. *API User’s Manual* e *Terms of Use for arXiv APIs*. [https://info.arxiv.org/help/api/user-manual.html](https://info.arxiv.org/help/api/user-manual.html); [https://info.arxiv.org/help/api/tou.html](https://info.arxiv.org/help/api/tou.html). Acesso em 13 ago. 2026.

#### [18] {#ref-18}

Directory of Open Access Journals. *API Documentation*. [https://doaj.org/api/docs](https://doaj.org/api/docs). Acesso em 13 ago. 2026.

#### [19] {#ref-19}

Open Archives Initiative. *Protocol for Metadata Harvesting, version 2.0*. [https://www.openarchives.org/pmh/](https://www.openarchives.org/pmh/).

#### [20] {#ref-20}

Unpaywall. *REST API*. [https://unpaywall.org/products/api](https://unpaywall.org/products/api). Acesso em 13 ago. 2026.

#### [21] {#ref-21}

OpenAlex. *API Documentation*; *Authentication*. [https://developers.openalex.org/](https://developers.openalex.org/); [https://developers.openalex.org/guides/authentication](https://developers.openalex.org/guides/authentication). Acesso em 13 ago. 2026.

#### [22] {#ref-22}

MacFarlane, J. *Pandoc User’s Guide*. [https://pandoc.org/MANUAL.html](https://pandoc.org/MANUAL.html). Acesso em 13 ago. 2026.

#### [23] {#ref-23}

Ollama. *API Documentation: Introduction and Authentication*. [https://docs.ollama.com/api/introduction](https://docs.ollama.com/api/introduction); [https://docs.ollama.com/api/authentication](https://docs.ollama.com/api/authentication). Acesso em 13 ago. 2026.

#### [24] {#ref-24}

ggml-org. *llama.cpp*. [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp). Acesso em 13 ago. 2026.

#### [25] {#ref-25}

NISO. *CRediT — Contributor Roles Taxonomy*. [https://credit.niso.org/](https://credit.niso.org/). Acesso em 13 ago. 2026.

#### [26] {#ref-26}

The Turing Way Community. *The Turing Way: a handbook for reproducible, ethical and collaborative data science*. [https://book.the-turing-way.org/](https://book.the-turing-way.org/). Acesso em 13 ago. 2026.

#### [27] {#ref-27}

Free Software Foundation. *GNU Affero General Public License, version 3*. [https://www.gnu.org/licenses/agpl-3.0.html](https://www.gnu.org/licenses/agpl-3.0.html).

#### [28] {#ref-28}

Creative Commons. *Attribution-ShareAlike 4.0 International*. [https://creativecommons.org/licenses/by-sa/4.0/](https://creativecommons.org/licenses/by-sa/4.0/).
