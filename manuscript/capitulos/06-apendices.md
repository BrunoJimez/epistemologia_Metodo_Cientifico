# Apêndices

## Apêndice A — Ferramentas matemáticas mínimas

### A.1 Proporção, escala e dimensão

Se `y = kx`, dobrar `x` dobra `y`; a razão `y/x` permanece `k`. Se `y = kx²`, dobrar `x` quadruplica `y`. Em gráfico log-log, uma lei de potência ideal `y=kxⁿ` tem inclinação `n`, mas ruído, faixa estreita e transformação dos erros podem enganar.

Dimensão pergunta que tipo de grandeza aparece; unidade escolhe um padrão. Comprimento tem dimensão `L` e pode ser expresso em metro ou centímetro. Na relação `T=2π√(L/g)`, `L/g` tem dimensão de tempo ao quadrado. A análise elimina formas impossíveis, mas não determina sozinha o fator `2π` nem o domínio de pequeno ângulo.

### A.2 Derivada como taxa

A velocidade média entre `t` e `t+Δt` é `Δs/Δt`. A derivada `ds/dt` é o limite dessa razão quando o intervalo tende a zero, quando o limite existe. Ela descreve uma regra local. Aceleração é `dv/dt = d²s/dt²`.

Para `s(t)=s₀+v₀t+½at²`, derivar fornece `v(t)=v₀+at`; derivar novamente fornece `a`. Esta é uma relação matemática. Medir uma “velocidade instantânea” exige intervalo finito e um modelo do sensor.

### A.3 Integral como acumulação

Se `v(t)` é velocidade, a mudança de posição é a área orientada sob a curva: `Δs=∫v(t)dt`. Somar retângulos cada vez menores aproxima a integral. O teorema fundamental conecta derivar e integrar sob condições adequadas.

O diagrama de Oresme torna intuitiva a acumulação, mas não deve ser identificado sem ressalvas com o formalismo integral posterior.

### A.4 Equação diferencial como regra local

Uma equação diferencial relaciona função e derivadas. `dT/dt=-k(T-Tₐ)` diz que a taxa de resfriamento é proporcional ao desvio térmico. Com `T(0)=T₀` e `k>0`, a solução é `T(t)=Tₐ+(T₀-Tₐ)e^{-kt}`. A equação, a condição inicial e o parâmetro formam o problema; sem eles não há previsão única.

### A.5 Conservação e fluxo: derivação do calor

Considere uma pequena fatia de barra. A variação da energia interna é fluxo que entra menos fluxo que sai. Para densidade `ρ`, calor específico `c` e temperatura `T`, energia por volume varia como `ρc ∂T/∂t`. A lei de Fourier dá fluxo `q=-κ∂T/∂x`. O balanço `ρc∂T/∂t=-∂q/∂x` produz

`∂T/∂t = α∂²T/∂x²`, com `α=κ/(ρc)`.

Origem: conservação mais relação constitutiva. Hipóteses: meio contínuo, parâmetros adequados e condução dominante. Condições de contorno especificam temperatura ou fluxo nas extremidades.

### A.6 Ondas, Fourier e Maxwell

Na corda ideal, tensão e densidade linear determinam `c`; a equação de onda permite superposição. Fourier mostra que, sob condições, um sinal pode ser representado por componentes senoidais. Espectro é representação, não coleção de pequenas ondas materiais escondidas.

As equações de Maxwell, em notação vetorial moderna, ligam divergência e rotação dos campos às fontes. Carga conserva-se; campos elétricos variáveis geram campo magnético e vice-versa; no vazio surgem ondas. A observação de Hertz e tecnologias posteriores conectam a derivação a sistemas físicos.

### A.7 Regressão e incerteza de parâmetro

Na regressão `y=Xβ+ε`, estimar `β` exige suposições sobre erro, independência e forma. Mínimos quadrados minimiza a soma de resíduos quadráticos. Intervalos-padrão usuais podem falhar com autocorrelação, variância não constante ou seleção posterior do modelo.

Para o plano inclinado, não force intercepto zero sem justificar `s₀` e o instante de liberação. Compare o ajuste livre com o restrito e mostre como a estimativa de aceleração muda.

### A.8 Dez passaportes de equações

| Exemplo | Origem | Hipótese central | Observável | Falha típica |
|---|---|---|---|---|
| `s=s₀+vt` | definição integrada | `v` constante | posição-tempo | resíduo curvo |
| `s=s₀+v₀t+½at²` | duas integrações | `a` constante | `s∝t²` no repouso | arrasto/impulso |
| `a=(5/7)g sen α` | dinâmica/energia | esfera maciça rolando | aceleração-ângulo | escorregamento |
| `T≈2π√(L/g)` | linearização | ângulo pequeno | período-comprimento | amplitude grande |
| `dT/dt=-k(T-Tₐ)` | lei empírica concentrada | corpo quase uniforme | curva exponencial | evaporação/gradiente |
| `∂T/∂t=α∂²T/∂x²` | conservação + Fourier | contínuo homogêneo | perfil térmico | convecção dominante |
| `I=P/(4πr²)` | conservação geométrica | fonte pontual isotrópica | intensidade-distância | absorção/fonte extensa |
| equação de onda | balanço local | pequenas deformações | modos/velocidade | não linearidade |
| Maxwell | princípios de campo | eletromagnetismo clássico | ondas, forças | escala quântica |
| Einstein | ação/consistência geométrica | gravitação métrica clássica | órbitas, luz, ondas | regime quântico |

## Apêndice B — Relatividade geral em segunda camada

### B.1 Métrica

O intervalo `ds²=gμν dxμ dxν` usa o tensor métrico `gμν` para definir durações, distâncias e cones de luz localmente. Em espaço-tempo plano, uma escolha de coordenadas produz a métrica de Minkowski; em gravitação, os componentes variam e não podem, em geral, ser transformados globalmente para a forma plana.

### B.2 Geodésica

Uma partícula em queda livre segue uma geodésica: trajetória que extremiza tempo próprio e obedece

`d²xμ/dτ² + Γμ_{αβ}(dxα/dτ)(dxβ/dτ)=0`.

Os símbolos de Christoffel `Γ` são construídos da métrica e de suas derivadas; podem ser não nulos por escolha de coordenadas mesmo sem curvatura. Por isso, “força gravitacional” e “coordenada acelerada” exigem distinção local/global.

### B.3 Curvatura

O tensor de Riemann mede a não comutatividade do transporte e a aceleração relativa de geodésicas. Contrações produzem tensor de Ricci `Rμν` e escalar `R`. O tensor de Einstein é `Gμν=Rμν-½Rgμν` e tem divergência covariante nula, compatível com conservação local.

### B.4 Energia-momento

`Tμν` reúne densidade de energia, densidade e fluxo de momento e tensões. Seu conteúdo depende do modelo de matéria. A equação de campo não entrega uma solução sem simetria, matéria e condições de contorno/iniciais.

### B.5 Limite e teste

No limite de campos fracos e velocidades baixas, componentes da métrica ligam-se ao potencial newtoniano e recuperam a equação de Poisson. Esse caso-limite testa coerência com uma teoria anterior em seu domínio; dados de Mercúrio, luz, relógios, pulsares e ondas gravitacionais testam a ponte empírica em regimes diversos.

## Apêndice C — Caderno de laboratório-modelo

### Página de identificação

- título e código do estudo;
- responsáveis e funções;
- pergunta, hipótese principal e rivais;
- data de início, local e riscos;
- versão do protocolo e repositório.

### Pré-registro mínimo

1. unidade experimental e amostra;
2. variáveis e procedimentos operacionais;
3. condições e controles;
4. número de repetições e regra de parada;
5. exclusões e dados ausentes;
6. modelos e gráficos;
7. decisão que cada resultado autoriza;
8. riscos de segurança e ética.

### Registro por sessão

| Campo | Conteúdo |
|---|---|
| início/fim | data, hora e fuso |
| ambiente | temperatura, iluminação, vibração |
| materiais | identificadores e versões |
| calibração | padrão, resultado, validade |
| dados brutos | arquivo imutável e checksum |
| desvios | o que mudou e por quê |
| observações | eventos não previstos |
| assinatura | operador e revisor |

### Encerramento

Preserve dado bruto; derive arquivos por script; associe figura a comando e versão; registre resultado negativo; diferencie análise planejada e exploratória; indique licença e dados pessoais.

## Apêndice D — Exercícios e respostas comentadas

### Exercícios

1. Explique por que `x+3=5` e `F=ma` são equações, mas têm funções diferentes.
2. Construa um argumento válido com premissa falsa.
3. Dê um contraexemplo a “todo objeto mais pesado cai mais rápido”.
4. Mostre dimensionalmente que `s=at` não pode representar posição sob aceleração constante.
5. Diferencie um gráfico reto de `s` contra `t` e de `s` contra `t²`.
6. Dê um caso em que repetição reduz dispersão, mas não viés.
7. Identifique hipótese auxiliar num teste de luz pelo inverso do quadrado.
8. Explique por que o teorema do grau médio não prova que Merton possuía laboratório moderno.
9. Classifique periélio de Mercúrio e eclipse de 1919 como retrodicção ou predição/teste.
10. Explique o papel de Grossmann sem separar ingenuamente “matemática” e “física”.
11. Uma prova Lean é aceita. Liste três coisas que ainda podem estar erradas na aplicação física.
12. Escreva a conclusão máxima permitida por dados simulados do plano inclinado.

### Respostas comentadas

1. Ambas afirmam igualdade. A primeira restringe incógnita num problema algébrico; a segunda relaciona grandezas físicas numa arquitetura dinâmica e requer ponte de medição.
2. “Todos os planetas são cubos; Marte é planeta; logo Marte é cubo.” A forma é válida; a primeira premissa é falsa.
3. Uma folha amassada e uma esfera mais pesada em condições de arrasto podem contrariar a regra; em vácuo ideal, massas diferentes têm a mesma aceleração gravitacional local.
4. `a` tem `L/T²`; multiplicar por `t` produz `L/T`, dimensão de velocidade. É preciso `t²` para comprimento.
5. Movimento uniforme torna o primeiro linear; aceleração constante desde repouso torna o segundo linear. Inspecionar resíduos é melhor que “olhar qual parece reto”.
6. Uma balança deslocada `+2 g` pode repetir com dispersão mínima; a média converge para o valor enviesado.
7. Fonte aproximadamente pontual, emissão estável, ausência de luz ambiente ou linearidade do detector.
8. O teorema é análise matemática idealizada. É preciso evidência documental de aparelho, procedimento, medição e confronto para alegar laboratório.
9. Mercúrio já era conhecido e funciona como retrodicção; o desvio da luz era consequência testada em nova campanha, embora medições e previsões anteriores tornem a história mais complexa.
10. Grossmann indicou e trabalhou o cálculo tensorial e a geometria diferencial; requisitos físicos influenciaram a escolha matemática e o formalismo reformulou o problema físico.
11. Tradução do fenômeno para o enunciado, valores medidos/parâmetros e adequação das idealizações.
12. Apenas que, sob o gerador declarado, o roteiro recupera a estrutura quadrática esperada. Nada foi medido no mundo.

# Glossário alfabético

**Abdução.** Inferência que propõe uma hipótese capaz de tornar um resultado esperado; não é dedução válida da hipótese a partir do resultado.

**Algoritmo.** Procedimento finito e especificado que transforma entradas em saídas.

**Axioma/postulado.** Enunciado adotado como ponto de partida de um sistema.

**Calibração.** Operação que estabelece relações entre indicações e valores/ incertezas de padrões, sob condições declaradas.

**Conceito.** Regra ou estrutura para classificar, relacionar e inferir.

**Condição de contorno.** Restrição espacial necessária para selecionar solução de uma equação diferencial.

**Condição inicial.** Estado do sistema em instante de referência.

**Contraexemplo.** Caso que torna falsa uma afirmação universal.

**Corolário.** Consequência próxima de um teorema.

**Dado.** Registro estruturado produzido por procedimento, com proveniência e metadados.

**Dedução.** Inferência em que premissas verdadeiras e forma válida tornam necessária a conclusão.

**Definição operacional.** Definição que liga o conceito a procedimento de identificação ou medição.

**Derivação.** Cadeia que obtém uma expressão ou previsão a partir de premissas e regras.

**Evidência.** Informação que altera o apoio comparativo entre hipóteses sob pressupostos declarados.

**Experimento.** Investigação com intervenção e controle planejados; nem toda ciência depende de experimento controlado.

**Expressão.** Combinação simbólica que designa valor quando interpretada.

**Fórmula.** Expressão compacta usada para calcular ou relacionar grandezas.

**Função.** Associação que atribui saídas a entradas segundo domínio e regra.

**Hipótese.** Proposição examinável, frequentemente comparada com rivais.

**Idealização.** Representação deliberadamente simplificada, com domínio e finalidade.

**Identidade.** Igualdade válida para todos os valores admissíveis.

**Incerteza de medição.** Parâmetro que caracteriza dispersão dos valores atribuídos ao mensurando com a informação disponível.

**Indução.** Inferência ampliativa de casos ou amostras para generalização/estimativa.

**Inferência.** Passagem de proposições a outra segundo regra ou padrão de apoio.

**Lei científica.** Regularidade expressa de modo geral dentro de domínio; não é estágio superior de teoria.

**Lema.** Resultado auxiliar usado numa demonstração.

**Medição.** Processo de obter valores razoavelmente atribuíveis a uma grandeza.

**Mensurando.** Grandeza que se pretende medir, especificada em detalhe suficiente.

**Modelo.** Representação seletiva de um sistema-alvo para explicar, prever, explorar ou intervir.

**Objetividade científica.** Resistência de afirmações a preferências idiossincráticas por controles públicos e crítica plural.

**Parâmetro.** Quantidade que caracteriza um modelo ou população e deve ser conhecida ou estimada.

**Predição.** Consequência para resultado ainda não usado na construção/ajuste relevante.

**Premissa.** Proposição usada como base de argumento.

**Princípio.** Enunciado de papel organizador amplo numa teoria.

**Proposição.** Conteúdo de uma afirmação capaz de verdade ou falsidade.

**Prova matemática.** Cadeia de inferências que estabelece um teorema em sistema; não confirma sozinha aplicação natural.

**Replicação.** Novo estudo voltado à mesma afirmação com novos dados; pode variar graus de independência.

**Reprodução computacional.** Obtenção dos mesmos resultados a partir dos mesmos dados e análise especificada.

**Resíduo.** Diferença entre valor observado e previsto pelo modelo.

**Retrodicção.** Consequência de uma teoria para evento ou dado anterior à formulação/ajuste relevante.

**Simulação.** Execução de modelo por algoritmo e código.

**Solidez.** Validade do argumento mais verdade de suas premissas.

**Teorema.** Proposição demonstrada a partir de axiomas/definições por regras aceitas.

**Teoria científica.** Arquitetura de conceitos, princípios, modelos, matemática, ligação à medição e evidência.

**Validade.** Impossibilidade de premissas verdadeiras e conclusão falsa numa forma dedutiva.

**Variável.** Símbolo ou característica que pode assumir valores.

**Verdade.** Propriedade atribuída a proposições; não é sinônimo de justificação ou consenso.

# Cronologia comentada

| Período | Nó preservado | O que permitiu | Limite da afirmação |
|---|---|---|---|
| Paleolítico | marcas deliberadas | memória externa possível | significado numérico debatido |
| IV milênio a.C. | fichas, medidas, escrita mesopotâmica | administração e cálculo registrado | não é origem única da escrita |
| II milênio a.C. | tábuas e papiros matemáticos | algoritmos, tabelas, agrimensura | notação moderna é reconstrução |
| séc. IV a.C. | Aristóteles | sistematização da demonstração | não inventa toda lógica |
| c. 300 a.C. | *Elementos* | organização axiomática | texto tem história editorial |
| helenismo | Arquimedes, Eratóstenes, Ptolomeu | matemática de equilíbrio, Terra e céu | fontes são parciais |
| sécs. I–VII | tradições chinesas e indianas | algoritmos, zero, astronomia | cronologias e autorias variadas |
| sécs. IX–XI | al-Khwārizmī, Ibn al-Haytham | álgebra retórica, óptica matemática | sem “inventor do método” |
| sécs. XII–XIII | traduções e universidades | circulação e crítica escolástica | transmissão não é cópia passiva |
| séc. XIV | Merton e Oresme | graus, velocidade média, gráficos | não laboratório moderno |
| 1543–1638 | Copérnico, Tycho, Kepler, Galileu | novos dados, órbitas e movimento | processo coletivo e controverso |
| 1557–1637 | Recorde, Viète, Descartes | igualdade e simbolismo algébrico | estabilização gradual |
| 1687 | Newton | unificação mecânica e gravitacional | cálculo também leibniziano |
| 1822–1873 | Fourier e Maxwell | calor, ondas e campos | notação atual é síntese posterior |
| séc. XIX | probabilidade e estatística | quantificação de variação | escolas rivais permanecem |
| 1879–1936 | Frege, Hilbert, Gödel, Turing | formalização e limites | não elimina semântica/aplicação |
| 1905–1915 | Einstein, Grossmann, Hilbert | relatividades e gravitação métrica | sem prova empírica definitiva |
| 1919–2016 | eclipse a ondas gravitacionais | testes em regimes diversos | cada teste carrega modelos auxiliares |
| 1945–2000 | computação e simulação | executar modelos complexos | erro numérico e de código |
| 2000–2024 | ciência aberta, Lean, crise de replicação | auditoria e prova formal | transparência não garante correção |
| 2025–20 ago. 2026 | AlphaProof e IA em problemas abertos | busca + verificação e descobertas relatadas | estado editorial e formalização importam |

## Nota bibliográfica crítica e trilhas de aprofundamento

Uma narrativa de longa duração precisa combinar síntese e estudos locais. Katz é útil como panorama da história da matemática, mas não substitui Robson, Imhausen, Plofker ou Chemla quando a afirmação depende de contexto e língua. [6](#ref-6) O material do British Museum sobre o Papiro Rhind serve como porta de entrada visual e institucional; a sustentação historiográfica principal vem da edição do papiro e da história contextual de Imhausen. [9](#ref-9) [88](#ref-88) Para a Mesopotâmia, Rochberg mostra por que traduzir categorias cuneiformes diretamente como a “natureza” moderna pode deformar a pergunta histórica. [87](#ref-87)

No estudo da prova, Hammack e Velleman ensinam técnicas contemporâneas; Lakatos mostra que a prática matemática também envolve conjecturas, contraexemplos e revisão de conceitos. [14](#ref-14) [15](#ref-15) [16](#ref-16) Os verbetes sobre platonismo e nominalismo impedem que a pergunta “inventada ou descoberta?” seja reduzida a duas caricaturas. [18](#ref-18) [19](#ref-19) Wigner e Hamming formularam versões influentes - e diferentes - do problema da eficácia da matemática; são pontos de partida para análise, não provas de uma metafísica. [21](#ref-21) [22](#ref-22)

Para ciência empírica, Tal ancora o vocabulário de medição; Pincock analisa representação matemática; Giere explicita a perspectiva dos modelos. [26](#ref-26) [65](#ref-65) [63](#ref-63) Godfrey-Smith e Chalmers são introduções, enquanto Popper e Kuhn devem ser lidos como programas históricos e filosóficos específicos, não como os dois únicos partidos possíveis. [28](#ref-28) [29](#ref-29) [30](#ref-30) [31](#ref-31) A síntese das National Academies sobre ciência e a pesquisa sobre aprendizagem lembram que definição didática de teoria não substitui a análise de práticas. [32](#ref-32) [34](#ref-34)

Na história pré-moderna, Archytas é um caso de matemática, música, política e mecânica cuja documentação fragmentária exige cautela. [40](#ref-40) Lindberg e a coletânea de Grant situam traduções e universidades, mas a historiografia recente pede ainda mais atenção a conexões interculturais. [46](#ref-46) [47](#ref-47) Ragep documenta ciências naturais em sociedades islâmicas, e Qidwai revisa criticamente as grandes narrativas de ciência e religião. [89](#ref-89) [90](#ref-90)

No laboratório, Montgomery oferece ferramentas de desenho experimental e Taylor introduz análise de erros; a terminologia final deste livro segue VIM/GUM. [66](#ref-66) [67](#ref-67) O manual de evidência científica de 2025 é relevante para avaliação pública de inferências, não apenas para tribunais. [69](#ref-69) Estudos de educação em física experimental mostram que estudantes precisam aprender iteração, diagnóstico e tomada de decisão, e não só seguir instruções. [70](#ref-70) *The Turing Way* amplia a cadeia para dados, software, colaboração e ética. [75](#ref-75)

Na formalização, Shannon separa quantidade de informação de significado; Frege, Hilbert, Gödel e Turing marcam programas distintos de lógica, axiomatização, incompletude e computabilidade. [76](#ref-76) [77](#ref-77) [78](#ref-78) [79](#ref-79) [80](#ref-80) O artigo técnico do Lean 4 complementa o manual vivo e permite distinguir arquitetura do sistema de uma versão da documentação. [95](#ref-95)

Para a relatividade geral, Norton, Stachel e Janssen/Renn ajudam a separar covariância, heurísticas físicas e reconstrução documental. [91](#ref-91) [92](#ref-92) O estudo de Corry, Renn e Stachel e o texto de Hilbert são indispensáveis para não resolver a prioridade Einstein-Hilbert por anedota. [93](#ref-93) [94](#ref-94) Finalmente, a publicação de exemplos do GUM em 2026 atualiza a prática metrológica, mas não altera retroativamente a definição do conjunto simulado deste livro. [97](#ref-97)

# Índice remissivo seletivo

**abdução**, 7, 26; **aceleração**, 14, 20, 27; **al-Khwārizmī**, 12; **algoritmo**, 11, 13, 28; **análise dimensional**, 14, Ap. A; **axioma**, 9, 29; **calibração**, 25, 27; **causalidade**, 7, 22; **conceito**, 1, 6; **contraexemplo**, 9, 29; **dedução**, 7–9; **Einstein**, 23, Ap. B; **equação**, 11–16; **evidência**, 6, 22, 26; **Fourier**, 16, Ap. A; **Galileu**, 20, 27; **Grossmann**, 23; **Hilbert**, 23, 29; **hipótese**, 22, 24; **IA**, 29; **Ibn al-Haytham**, 18; **incerteza**, 25–27; **indução**, 7; **instrumento**, 1, 20, 25; **Lean**, 29; **lei**, 21–22; **Maxwell**, 16; **medição**, 1, 25; **Merton**, 19; **modelo**, 1, 14, 22, 28; **Newton**, 16, 21; **objetividade**, 2, 30; **Oresme**, 19; **plano inclinado**, 20, 27; **prova**, 9, 29; **regressão**, 26–27; **replicação**, 24, 27; **resíduo**, 26–27; **simulação**, 28; **teoria**, 22–23; **verdade**, 6, 9.
