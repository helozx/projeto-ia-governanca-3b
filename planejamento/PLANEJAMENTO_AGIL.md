# Planejamento Ágil e Quadro Kanban

## 1. Objetivo do produto

Entregar um projeto escolar verificável sobre ética, viés e governança em algoritmos de crédito, contendo relatório, planejamento ágil, base simulada, notebook executável e histórico de participação no GitHub.

## 2. Papéis da equipe

| Pessoa | Papel Scrum | Decisões e atividades |
|---|---|---|
| Lara | Product Owner | Define prioridades, esclarece requisitos e aceita ou rejeita entregas |
| Kilmes | Scrum Master | Facilita as reuniões, controla WIP e remove impedimentos |
| Antônio | Dev de Dados | Produz CSV, código Python, métricas e gráficos |
| **[NOME DO 4º INTEGRANTE]** | Dev e QA | Revisa texto, testa notebook e confere GitHub/Trello |

Todos podem desenvolver e revisar. Os papéis indicam a responsabilidade principal, não exclusividade.

## 3. Eventos Scrum adaptados ao trabalho escolar

| Evento | Duração | Finalidade |
|---|---:|---|
| Planejamento da sprint | 30 min | Selecionar histórias e dividir responsabilidades |
| Daily | 5 min por dia | Dizer o que foi feito, próximo passo e impedimento |
| Revisão | 20 min | Product Owner valida os critérios de aceitação |
| Retrospectiva | 15 min | Registrar o que funcionou e o que melhorar |

## 4. Definition of Ready

Uma história só entra em **A Fazer** quando possui:

- objetivo compreendido pela equipe;
- responsável inicial;
- critérios de aceitação;
- dependências identificadas;
- estimativa em pontos.

## 5. Definition of Done

Uma história está **Concluída** quando:

- atende a todos os critérios de aceitação;
- foi revisada por outra pessoa;
- não contém dados pessoais reais;
- arquivo abre ou código executa sem erro;
- alteração foi registrada em commit identificado;
- Product Owner confirmou a entrega.

## 6. Histórias de usuário e Planning Poker

A estimativa utiliza a sequência Fibonacci: **1, 2, 3, 5, 8 e 13**. Os pontos representam esforço relativo, complexidade e incerteza.

| ID | História de usuário | Critérios de aceitação | Pontos | Responsável |
|---|---|---|---:|---|
| US01 | Como estudante, quero entender o caso Apple Card para apresentar um exemplo real sem afirmar algo que a investigação não comprovou. | Contexto, reclamações e resultado oficial descritos; fonte oficial incluída; diferença entre alegação e conclusão destacada. | 5 | Lara |
| US02 | Como leitor, quero identificar possíveis falhas nos dados e no modelo para entender a origem do viés. | Pelo menos cinco falhas explicadas; presença de viés histórico, amostra e proxies; linguagem compreensível. | 3 | Lara |
| US03 | Como cidadão, quero conhecer os riscos de exclusão digital para saber quem pode ser prejudicado. | Barreiras de aparelho, internet, acessibilidade e ausência de histórico discutidas; medidas de inclusão propostas. | 3 | Kilmes |
| US04 | Como regulador, quero regras de governança para reduzir decisões injustas. | Inclui avaliação de impacto, auditoria, explicação, recurso, monitoramento e proteção de dados; relação com LGPD. | 5 | Kilmes |
| US05 | Como cientista de dados, quero uma base CSV fictícia para testar indicadores sem expor pessoas reais. | Arquivo com 40 ou mais linhas; dicionário compreensível; nenhum dado pessoal real; viés didático declarado. | 3 | Antônio |
| US06 | Como professor, quero um notebook comentado que leia a base e apresente resultados reproduzíveis. | Executa no Colab; lê o CSV; mostra amostra e tipos; calcula taxas por grupo; gera gráfico; contém conclusão. | 5 | Antônio |
| US07 | Como equipe, quero um Kanban com limites de WIP para evitar muitas tarefas iniciadas ao mesmo tempo. | Listas definidas; cartões possuem responsável e pontos; WIP visível; nenhuma coluna ultrapassa o limite. | 3 | Kilmes |
| US08 | Como avaliador, quero um repositório organizado com branches e commits individuais para verificar a participação. | README presente; branches nomeadas; pelo menos dois commits reais por integrante; contribuições documentadas. | 3 | **[4º INTEGRANTE]** |
| US09 | Como apresentador, quero revisar todos os links e arquivos para evitar falhas durante a entrega. | Links abrem para leitores; notebook executado do início ao fim; nomes preenchidos; checklist assinado. | 2 | Equipe |

**Total estimado:** 32 pontos.

## 7. Planejamento das sprints

### Sprint 1 — Pesquisa e estrutura

**Meta:** concluir a base conceitual e preparar o ambiente de trabalho.

- US01 — Caso real.
- US02 — Falhas nos dados e modelo.
- US03 — Exclusão digital.
- US05 — Base CSV.
- US07 — Kanban.

### Sprint 2 — Implementação, governança e entrega

**Meta:** finalizar o laboratório, publicar o projeto e validar os critérios.

- US04 — Regras de governança.
- US06 — Notebook.
- US08 — GitHub e evidências.
- US09 — Revisão final.

## 8. Fluxo Kanban e limites de WIP

| Lista | Regra de entrada | Limite WIP | Regra de saída |
|---|---|---:|---|
| Backlog | História registrada e priorizada | Sem limite | Atende à Definition of Ready |
| A Fazer | Pronta para iniciar na sprint | 5 | Um responsável começa o trabalho |
| Em Andamento | Trabalho ativo | **2** | Critérios implementados |
| Em Revisão | Aguardando teste ou validação | **2** | Revisor e PO aprovam |
| Concluído | Atende à Definition of Done | Sem limite | Não volta sem novo problema registrado |

### Política de WIP

Se **Em Andamento** já tiver dois cartões, ninguém inicia uma terceira tarefa. A equipe ajuda a concluir ou desbloquear um cartão existente. Se **Em Revisão** atingir dois cartões, a prioridade é revisar antes de iniciar trabalho novo. Essa regra reduz espera, retrabalho e tarefas abandonadas.

## 9. Estado inicial do quadro

| Backlog | A Fazer | Em Andamento | Em Revisão | Concluído |
|---|---|---|---|---|
| US08 GitHub | US03 Exclusão digital | US01 Caso real | — | — |
| US09 Revisão final | US04 Governança | US05 Base CSV | — | — |
| — | US06 Notebook | — | — | — |
| — | US07 Kanban | — | — | — |
| — | US02 Falhas e riscos | — | — | — |

## 10. Modelo de cartão no Trello

**Título:** `US06 — Criar notebook de análise de viés`  
**Descrição:** Como professor, quero um notebook comentado que leia a base e apresente resultados reproduzíveis.  
**Responsável:** Antônio  
**Estimativa:** 5 pontos  
**Checklist:**

- importar pandas e matplotlib;
- carregar o CSV;
- verificar nulos e duplicados;
- calcular taxa geral;
- comparar grupos;
- gerar gráfico;
- registrar conclusão;
- pedir revisão de outro integrante.

## 11. Retrospectiva sugerida

| Continuar | Parar | Começar |
|---|---|---|
| Revisão por outra pessoa antes do merge | Iniciar várias tarefas ao mesmo tempo | Registrar impedimentos na daily |
| Commits pequenos e identificáveis | Deixar links para a última hora | Executar o notebook em conta diferente |
| Critérios de aceitação objetivos | Copiar informações sem conferir a fonte | Capturar evidências do Trello e GitHub |

