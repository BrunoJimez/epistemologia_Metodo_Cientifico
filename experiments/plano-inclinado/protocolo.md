# Protocolo replicável — plano inclinado

**Status:** protocolo didático. **Dados de demonstração: simulados.**  
**Supervisão:** obrigatória para adolescentes.  
**Fontes:** Galileu, *Duas novas ciências*; Straulino, “Reconstruction of Galileo Galilei's Experiment: The Inclined Plane”, 2008, DOI 10.1088/0031-9120/43/3/012.

## 1. Pergunta

Em uma rampa fixa, a posição de uma esfera liberada aproximadamente do repouso é melhor descrita como proporcional a `t` ou a `t²`?

## 2. Modelos rivais

- uniforme: `s=β₀+β₁t`;
- aceleração constante: `s=β₀+β₂t²`;
- físico geral: `s=s₀+v₀t+½at²`;
- rival material: aceleração variável por geometria, escorregamento ou perdas.

## 3. Definições

`s`: coordenada do centro da esfera ao longo do canal (m). `t`: intervalo entre eventos operacionais (s). `v=ds/dt` (m/s). `a=dv/dt` (m/s²). Evento inicial: primeiro quadro após retirada completa da barreira. Evento final: primeiro quadro em que o centro cruza a marca.

## 4. Materiais

Canaleta reta de 1,2–2,0 m; base fixável; esfera; fita; régua; calços; recipiente acolchoado; celular e tripé; medidor de ângulo. Opcional: relógio de água com recipiente, válvula, copos e balança.

## 5. Segurança e montagem

Fixe a rampa entre 5° e 10°, a menos de 0,5 m do chão. Isole a área. Coloque retenção. Teste a esfera em velocidade baixa. Marque cinco posições. Filme escala no plano da trajetória e câmera perpendicular.

## 6. Pré-registro

Declare antes: esfera/ângulo; mínimo de oito repetições por posição; taxa de quadros; regra de leitura; exclusões; modelos; gráficos; como tratar intercepto; critério de interpretação. Preserve desvios.

## 7. Procedimento por vídeo

1. Registre ambiente, montagem, diâmetro, massa, ângulo e arquivo.
2. Grave a rampa e a escala sem mover a câmera.
3. Posicione a esfera na barreira, sem comprimi-la.
4. Inicie vídeo e retire a barreira lateralmente.
5. Deixe a esfera cair na retenção.
6. Repita oito vezes; alterne a ordem das distâncias se usar marcas finais separadas.
7. Conte quadros segundo regras pré-registradas.
8. Calcule `t=(quadro_fim-quadro_inicio)/fps`.
9. Marque tentativas inválidas sem apagá-las.

## 8. Procedimento com relógio de água

Calibre massa coletada contra intervalos de vídeo. Em cada ensaio, abra o fluxo no evento inicial e feche no final. Pese água. Converta massa em tempo com a curva de calibração. Registre simultaneidade e variação de vazão. O método apenas reconstrói uma possibilidade histórica.

## 9. Análise

Calcule contagem, média e desvio por posição; quantifique resolução temporal; trace `s×t`, `s×t²` e resíduos; ajuste os dois modelos; estime `a=2β₂` quando adequado; compare `a` com `(5/7)g sen α` para esfera maciça ideal; faça sensibilidade ao intercepto e exclusões.

## 10. Interpretação e replicação

Prefira: “o quadrático descreveu melhor estes dados segundo resíduos e RMSE”. Não escreva “a lei foi provada”. Repita com novos operadores, ângulos e esferas. Registre reprodução do código separadamente de replicação com novos dados.

