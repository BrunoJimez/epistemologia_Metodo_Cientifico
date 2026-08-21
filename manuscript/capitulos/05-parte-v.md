# Parte V — O laboratório corrigível

## 24. O método científico como ciclo, não receita

Não há uma sequência universal em que toda ciência primeiro observa, depois formula hipótese e por fim experimenta. Astronomia e geologia não controlam seus objetos como um ensaio de bancada; epidemiologia combina observação, modelos e quase-experimentos; física de partículas depende de instrumentos orientados por teoria; ciência exploratória pode encontrar uma regularidade antes de explicá-la.

O framework em doze núcleos organiza dependências sem engessar a prática:

1. fenômeno e problema;
2. pergunta delimitada;
3. conceitos e definições operacionais;
4. hipótese e rivais;
5. idealizações e modelo;
6. matemática e derivação;
7. previsão ou retrodicção;
8. desenho e pré-registro quando útil;
9. instrumento, calibração e medição;
10. dados, metadados e incerteza;
11. confronto, estatística e interpretação;
12. crítica, replicação e revisão.

As setas voltam. Um padrão nos resíduos pode levar ao sensor, à condição inicial, ao modelo de ruído ou à hipótese. [35](#ref-35)

**Erro escolar comum.** Procurar “o método científico” como algoritmo que transforma qualquer pergunta em verdade. Métodos são famílias de controles adaptadas a objetos e riscos de erro.

**Veja em sua vida.** Para saber se dormir mais melhora seu tempo de reação, não comece pelo aplicativo. Defina “dormir mais”, “tempo de reação”, janela de observação, fatores de confusão, regra de exclusão e interpretação permitida.

**Caderno científico.** Registre antes, durante e depois: propósito, versões, materiais, desvios do plano, decisões e resultados negativos. O caderno é uma extensão da memória e uma superfície de auditoria.

## 25. Medição, calibração, erro e incerteza

**Medição** é um processo de obter valores que podem ser razoavelmente atribuídos a uma grandeza. O **mensurando** é a grandeza pretendida: não “a esfera”, mas “o tempo entre a liberação operacional e a passagem da marca de 0,80 m”. **Calibração** estabelece, sob condições declaradas, relações entre indicações e padrões; não é sinônimo de ajuste nem de verificação. [81](#ref-81)

Erro de medição é a diferença entre valor medido e valor de referência; muitas vezes o erro particular é desconhecido. **Incerteza** é um parâmetro não negativo que caracteriza a dispersão dos valores atribuídos ao mensurando com a informação disponível. Ela inclui componentes avaliados por repetição (tipo A) e por resolução, calibração, especificação ou conhecimento prévio (tipo B). [82](#ref-82)

Exemplo: vídeo a 60 quadros por segundo tem passo nominal de `1/60 s ≈ 0,0167 s`. Isso não significa automaticamente incerteza de exatamente meio quadro; o instante de liberação, obturador, seleção do quadro e taxa real precisam entrar no modelo.

**Precisão** descreve proximidade entre resultados repetidos; **exatidão** é conceito qualitativo relacionado à proximidade do valor verdadeiro; **viés** é componente sistemática. Uma balança pode repetir `102,0 g` e estar deslocada `+2,0 g`.

**Propagação simples.** Se `v = s/t`, pequenas incertezas independentes podem ser aproximadas por

`u(v)/v ≈ √[(u(s)/s)² + (u(t)/t)²]`.

A fórmula depende de linearização e independência. Correlações exigem covariâncias. Um orçamento de incerteza declara entradas, distribuições assumidas e como foram combinadas. [83](#ref-83)

**Experimento seguro.** Meça o mesmo livro com duas réguas, troque operadores e orientação. Separe variação de leitura, resolução e possível erro de zero.

## 26. Estatística, inferência e modelos rivais

Dados variam. A estatística descreve essa variação e quantifica o que diferentes modelos esperariam; ela não substitui desenho nem qualidade de medição.

Para valores `x₁...xₙ`, a média é `x̄ = Σxᵢ/n`. O desvio-padrão amostral é `s = √[Σ(xᵢ-x̄)²/(n-1)]`. A incerteza-padrão da média frequentemente é estimada por `s/√n` sob independência e estabilidade; repetir uma medição com o mesmo viés reduz ruído, não corrige o viés.

### Um modelo probabilístico simples

Se resultados binários independentes têm probabilidade constante `p`, o número de sucessos em `n` tentativas segue modelo binomial. “Independentes” e “p constante” são hipóteses. Em uma moeda real, desgaste, operador e seleção de lançamentos podem violá-las.

### Regressão como inferência de parâmetros

No plano inclinado, compare:

- linear no tempo: `s = β₀ + β₁t + ε`;
- quadrático: `s = β₀ + β₂t² + ε`;
- modelo físico completo: `s = s₀ + v₀t + ½at² + ε`.

O ajuste estima parâmetros. **Resíduo** é `observado - previsto`; gráficos de resíduos mostram curvatura, variância crescente, atrasos e pontos influentes. Um `R²` alto pode coexistir com estrutura errada, especialmente quando ambas as variáveis crescem com o tempo. [68](#ref-68)

**Distinção essencial.** Significância estatística não mede tamanho, importância, ausência de viés nem probabilidade de a hipótese ser verdadeira. Intervalos e probabilidades dependem do modelo e do procedimento.

**Modelos rivais.** Pré-especifique qual observação distingue as alternativas. Compare erro de previsão, resíduos e plausibilidade física; penalize flexibilidade excessiva. Um modelo mais complexo pode ajustar ruído.

## 27. Replicação completa do plano inclinado

Este estudo transforma o ciclo inteiro num protocolo seguro. Adolescente deve trabalhar com supervisão; a rampa fica baixa, estável e longe de escadas, vidro e circulação. Não use esferas pesadas, rampas altas nem cronômetros ligados à rede exposta.

### 27.1 Fenômeno, pergunta e hipóteses

Uma esfera liberada numa rampa percorre distâncias crescentes em intervalos iguais. Pergunta: **no trecho e nas condições definidos, posição ao longo da rampa é melhor descrita como linear em `t` ou em `t²`?**

- `H₁`, uniforme: `s = s₀ + vt`;
- `H₂`, aceleração constante: `s = s₀ + v₀t + ½at²`;
- rival material: aceleração varia por deslizamento, irregularidade ou rampa curva.

### 27.2 Definições e idealizações

`s` é a coordenada do centro da esfera ao longo do canal, em metros; `t` é o intervalo entre liberação e passagem da marca; `v=ds/dt`; `a=dv/dt`. Idealizamos esfera rígida, rampa reta, ângulo constante, rolamento sem escorregar, resistência pequena e liberação sem impulso. Com `a` constante, integração fornece `s=s₀+v₀t+½at²`; para `s₀=0` e `v₀≈0`, `s∝t²`.

### 27.3 Materiais e montagem

- canaleta ou perfil reto de 1,2 a 2,0 m, preso a base estável;
- esfera de aço ou vidro com diâmetro registrado;
- calços, fita, régua de 1 mm, nível ou aplicativo de inclinação;
- recipiente de retenção com pano;
- celular em tripé, enquadramento fixo, 60 fps ou mais;
- opcional histórico: recipiente de água, válvula simples, copos e balança.

Eleve uma extremidade entre 5° e 10°. Marque `s = 0,20; 0,40; 0,60; 0,80; 1,00 m`, medidos no canal. Filme uma régua no mesmo plano da trajetória. Fixe a rampa; teste a retenção.

### 27.4 Pré-registro didático

Antes dos dados, escreva: hipótese principal; número de repetições (mínimo 8 por distância); esfera, ângulo e operador; taxa de quadros; regra de início/fim; exclusões permitidas (por exemplo, esfera sai do canal); modelos; gráfico e interpretação. Desvios permanecem no registro.

### 27.5 Método histórico e método moderno

**Relógio de água:** libere esfera e fluxo tão simultaneamente quanto possível; interrompa no evento final; pese ou meça água. Calibre massa de água por tempo com repetições. É uma reconstrução inspirada no texto, não dados originais de Galileu.

**Vídeo:** câmera perpendicular ao plano, distante para reduzir perspectiva; iluminação curta; marcador de escala; liberação mecânica simples. Conte quadros e divida pela taxa verificada. Guarde arquivo, metadados e código de leitura.

### 27.6 Tabela e repetições

Registre em colunas:

- identificação: `run_id`, `data_hora`, `operador`;
- material: `esfera`, `diametro_m`, `massa_kg`, `angulo_deg`;
- evento: `posicao_m`, `metodo`, `fps`, `quadro_inicio`, `quadro_fim`, `tempo_s`;
- auditoria: `observacoes`, `excluida`, `motivo_exclusao`.

Não apague ensaios; marque exclusões.

### 27.7 Análise

1. resuma média, desvio-padrão e contagem por posição;
2. componha resolução temporal e repetibilidade;
3. trace `s` contra `t` e `s` contra `t²`;
4. ajuste modelos linear e quadrático sob a mesma regra;
5. trace resíduos contra tempo e valor previsto;
6. estime `a = 2β₂` quando intercepto e `v₀` forem tratados adequadamente;
7. compare com esfera rolando: `a=(5/7)g sen α` para esfera maciça ideal;
8. faça análise de sensibilidade incluindo/excluindo ensaios pré-especificados.

### 27.8 Exemplo — DADOS SIMULADOS

| `s` (m) | tempo médio simulado (s) | desvio simulado (s) |
|---:|---:|---:|
| 0,20 | 0,506 | 0,010 |
| 0,40 | 0,714 | 0,012 |
| 0,60 | 0,874 | 0,013 |
| 0,80 | 1,011 | 0,014 |
| 1,00 | 1,130 | 0,016 |

Esses números foram gerados para ensinar análise; **não são medidas reais nem históricas**. O conjunto completo e a semente estão em `dados-simulados.csv` e `analise.py`.

### 27.9 Erros sistemáticos e interpretação

Possíveis fontes: rampa arqueada, ângulo mal medido, perspectiva, taxa de quadros variável, liberação com impulso, esfera escorregando, marcas espessas, atraso do relógio de água e seleção tendenciosa de tentativas. A rotação desvia a aceleração do modelo de bloco deslizante; o momento de inércia depende da distribuição de massa.

Conclusão permitida: “Nestas condições, o modelo quadrático produziu resíduos menores e menos estruturados que o linear.” Conclusão excessiva: “Provamos definitivamente a lei universal da queda.”

### 27.10 Replicação e extensão

Repita com ângulos, esferas e operadores diferentes. Uma **repetição** interna estima variação; uma **replicação** independente reconstrói o teste; uma **reprodução computacional** executa análise com os mesmos dados. Extensões: testar `a` contra `sen α`, comparar esfera maciça e oca, estimar perda por rolamento e investigar taxa de quadros. [33](#ref-33)

## 28. Simulação: modelo, algoritmo, código e hardware

Uma simulação executa regras de um modelo. A cadeia é: sistema-alvo → modelo conceitual → equações → discretização/algoritmo → código → compilador/biblioteca → hardware → saída → análise. Cada seta pode introduzir erro.

Na equação do calor, substituímos derivadas por diferenças em uma malha. Passos muito grandes podem tornar um método numericamente instável embora a equação física esteja correta. Verificação pergunta “resolvemos corretamente as equações escolhidas?”; validação pergunta “as equações representam o alvo para esta finalidade?”. [64](#ref-64)

**Distinção essencial.** Dados simulados não são observações. Eles ajudam a testar análise, explorar consequências, calibrar desenho e comparar algoritmos. Só informam diretamente sobre o mundo por meio da adequação do modelo e de parâmetros ligados a medições.

**Como uma IA pode errar aqui.** Pode gerar código executável que conserva a grandeza errada, mistura unidades ou usa condições de contorno implícitas. Testes unitários não substituem testes de convergência, balanços físicos e comparação com casos analíticos.

**Exercício.** Para uma simulação de epidemia, liste uma escolha em cada camada e uma observação externa necessária para validá-la.

## 29. Provas formais e inteligência artificial

Um assistente de prova como Lean representa definições e teoremas numa linguagem formal. Táticas constroem termos que um núcleo pequeno verifica. Isso reduz certas lacunas humanas, mas a garantia permanece condicional à formalização, aos axiomas, ao núcleo, ao compilador e ao hardware. [71](#ref-71) [72](#ref-72)

Em 2025-2026, sistemas de IA passaram a combinar busca, aprendizado por reforço, autoformalização e verificadores. AlphaProof resolveu três dos cinco problemas não geométricos da Olimpíada Internacional de Matemática de 2024; o artigo foi publicado on-line em 2025 e ganhou versão de registro em 2026. O verificador confirma as provas formalizadas, não a correção automática da tradução de toda frase informal. [73](#ref-73)

Em maio de 2026, a OpenAI divulgou uma refutação gerada por modelo de uma conjectura de Erdős sobre distâncias unitárias, acompanhada por prova e avaliação externa. Em 1º de agosto, divulgou dez avanços adicionais. São marcos institucionais recentes; cada resultado deve ser avaliado pelo texto matemático, revisão especializada e estado editorial, não pela autoridade do comunicado. [74](#ref-74) [96](#ref-96)

**IA neuro-simbólica** combina modelos aprendidos com representação ou verificação simbólica. Ela pode sugerir lemas, buscar contraexemplos e controlar provas. Ainda pode formular o teorema errado, omitir uma hipótese física ou citar uma versão inexistente.

**O que a matemática garante.** Uma prova formal aceita garante derivabilidade do enunciado formal no sistema implementado.

**O que não garante.** Que o enunciado formal traduz corretamente a intenção, que descreve a natureza ou que dados e instrumentos são adequados.

## 30. Como pensar e ensinar como cientista

Pensar cientificamente não é recitar “observe, formule, teste”. É sustentar uma cadeia auditável e saber onde cada garantia termina.

Use a frase de doze partes:

> Diante de **[fenômeno]**, pergunto **[pergunta]**; defino **[grandezas]** por **[procedimentos]**; comparo **[hipóteses]**; idealizo **[sistema]**; represento-o por **[modelo/equação]**; derivo **[previsão]**; observo com **[instrumento/calibração]**; registro **[dados/metadados]**; quantifico **[incerteza]**; confronto por **[análise]**; interpreto dentro de **[domínio]** e abro **[replicação/revisão]**.

### Um experimento cotidiano completo

Pergunta: chá esfria mais rapidamente em caneca larga? Defina temperatura central, intervalo e ambiente; compare recipientes; alterne ordem; calibre sensores; ajuste `T(t)=Tₐ+(T₀-Tₐ)e^{-kt}`; examine resíduos; não conclua além dos materiais e condições testados. O modelo pode falhar por evaporação, gradiente interno e ambiente variável.

### Rubrica de maturidade

O aprendiz progride quando consegue: separar observação de inferência; explicitar unidades; imaginar rivais; registrar decisões; localizar um viés que repetição não resolve; interpretar resíduos; distinguir prova de teste; reproduzir análise; criticar a própria afirmação mais forte.

**Como ensinar.** Comece por contrastes e objetos reais; peça previsões antes do resultado; valorize um erro bem localizado; faça alunos trocar cadernos e replicar; use história para mostrar escolhas, não para decorar heróis.

**Epílogo — A ponte corrigível.** Uma teoria científica não elimina mediações humanas. Ela as torna criticáveis. A objetividade é uma conquista de procedimentos, diversidade de crítica, instrumentos rastreáveis e disposição institucional para corrigir. A certeza matemática é poderosa dentro do que foi formalizado; a confiança empírica é graduada, histórica e renovável. Saber onde uma afirmação pode quebrar não a enfraquece: é o que a torna ciência.
