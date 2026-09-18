# Relatório de Impacto e Governança

## Algoritmos de crédito e risco de viés: o caso Apple Card/Goldman Sachs

**Disciplina:** Ética em Inteligência Artificial  
**Turma:** 3º Ano B — Ensino Médio Técnico  
**Bimestre:** 3º Bimestre  
**Equipe:** Kilmes, Lara, Antônio e **[NOME DO 4º INTEGRANTE]**  
**Data:** **[PREENCHER DATA DE ENTREGA]**

---

## Resumo

Este relatório analisa riscos éticos em algoritmos usados para decidir aprovação, limite e condições de crédito. O estudo parte do caso Apple Card, lançado em 2019 pela Apple com concessão de crédito realizada pelo Goldman Sachs. Usuários relataram diferenças muito grandes entre limites oferecidos a homens e mulheres, além da dificuldade de obter uma explicação clara sobre as decisões. O Departamento de Serviços Financeiros do Estado de Nova York investigou o caso e não encontrou evidência de discriminação ilegal intencional ou de impacto desigual nos dados analisados. Mesmo assim, o órgão identificou falhas de transparência e atendimento e destacou que modelos de crédito podem reproduzir desigualdades históricas. O trabalho descreve possíveis falhas nos dados e no modelo, discute exclusão digital e propõe regras de governança baseadas em transparência, auditoria, revisão humana, proteção de dados e monitoramento contínuo.

**Palavras-chave:** inteligência artificial; crédito; viés algorítmico; governança; transparência; LGPD.

## 1. Introdução

Bancos e empresas de tecnologia usam sistemas automatizados para analisar grande quantidade de dados e estimar o risco de uma pessoa não pagar uma dívida. Esses sistemas podem acelerar a análise, reduzir custos e padronizar decisões. Porém, uma decisão automática também pode negar oportunidades econômicas importantes. Sem crédito, uma pessoa pode ter dificuldade para estudar, abrir um negócio, comprar uma casa ou lidar com uma emergência.

Um algoritmo não se torna justo apenas porque ignora explicitamente raça ou gênero. Variáveis como endereço, profissão, renda, histórico bancário, tipo de aparelho, comportamento de consumo e estabilidade de conexão podem funcionar como substitutos indiretos de características sociais protegidas. Além disso, dados históricos registram desigualdades já existentes. Quando o modelo aprende com esse passado sem controles adequados, pode repetir a desigualdade em escala.

Este relatório investiga a seguinte questão: **como impedir que algoritmos de crédito reproduzam exclusões históricas e tomem decisões opacas, mesmo quando atributos protegidos não aparecem diretamente no modelo?**

## 2. Objetivos

### 2.1 Objetivo geral

Analisar os riscos de viés e as falhas de governança em decisões automatizadas de crédito, usando o caso Apple Card como referência real.

### 2.2 Objetivos específicos

- Descrever a controvérsia e o resultado da investigação oficial.
- Identificar possíveis falhas nos dados, no modelo e no atendimento ao consumidor.
- Explicar como a exclusão digital pode afetar a concessão de crédito.
- Propor regras de regulamentação e controles internos.
- Demonstrar, em uma base simulada, como medir diferenças de aprovação entre grupos.

## 3. Caso real: Apple Card e Goldman Sachs

### 3.1 Contexto

A Apple e o Goldman Sachs lançaram o Apple Card em agosto de 2019. A solicitação era feita pelo iPhone e a análise do crédito ficava sob responsabilidade do banco. Em novembro daquele ano, consumidores publicaram relatos de que mulheres teriam recebido limites muito menores do que homens da mesma família. Um dos relatos afirmou que o limite concedido ao marido foi vinte vezes maior do que o oferecido à esposa. Também houve reclamações de que o atendimento não conseguia explicar os fatores responsáveis pelas diferenças.

A repercussão levou o Departamento de Serviços Financeiros do Estado de Nova York, o NYDFS, a abrir uma investigação. O órgão analisou documentos, entrevistou consumidores e examinou dados de quase 400 mil candidatos do estado de Nova York.

### 3.2 Resultado da investigação

O relatório oficial, publicado em março de 2021, **não encontrou evidência de discriminação ilegal deliberada nem de impacto desigual entre homens e mulheres com características de crédito equivalentes**. O órgão verificou que diferenças em renda, endividamento, pontuação, utilização de crédito e histórico individual podiam explicar as decisões examinadas.

Esse resultado não significa que o caso não tenha valor como estudo de ética em IA. A investigação encontrou problemas importantes de governança:

- pouca transparência para explicar limites e condições oferecidas;
- atendimento inicialmente incapaz de esclarecer decisões complexas;
- processo lento para contestar ou pedir revisão do limite;
- lançamento do produto sem preparo suficiente para resultados que surpreendessem os consumidores;
- risco de dados financeiros aparentemente neutros carregarem desigualdades históricas.

Assim, o caso deve ser apresentado corretamente como uma **controvérsia real de possível viés e uma falha confirmada de transparência e governança**, e não como prova de que o Goldman Sachs praticou discriminação ilegal.

## 4. Como surge o viés em algoritmos de crédito

### 4.1 Viés histórico nos dados

Os registros usados para treinar modelos representam decisões e condições sociais do passado. Grupos que tiveram menor acesso a bancos, imóveis, empregos formais e crédito barato podem possuir históricos financeiros menores ou mais instáveis. O modelo pode interpretar essa desigualdade histórica como sinal individual de risco.

### 4.2 Amostra pouco representativa

Uma base com poucos exemplos de jovens, moradores de regiões periféricas, trabalhadores informais ou pessoas sem histórico bancário pode produzir previsões piores para esses grupos. A precisão média pode parecer boa e esconder erros concentrados em uma minoria.

### 4.3 Variáveis substitutas

Excluir gênero, raça ou origem do conjunto de dados não elimina automaticamente o viés. CEP, região, escola, profissão, padrão de compras e aparelho utilizado podem manter forte relação com grupos sociais específicos. Essas variáveis são chamadas de *proxies* quando representam indiretamente uma característica que o modelo não deveria usar para discriminar.

### 4.4 Definição inadequada do objetivo

O modelo pode ser treinado apenas para aumentar lucro ou reduzir inadimplência. Se não houver uma meta explícita de equidade, ele pode favorecer pessoas já atendidas pelo sistema financeiro e rejeitar candidatos com pouco histórico, mesmo quando seriam capazes de pagar.

### 4.5 Falta de explicabilidade

Modelos muito complexos podem fornecer uma nota sem mostrar de forma compreensível por que a decisão foi tomada. Isso impede o consumidor de corrigir dados errados, melhorar sua situação ou contestar a decisão. Também dificulta o trabalho de auditores e reguladores.

### 4.6 Avaliação incompleta

Testar somente a acurácia geral é insuficiente. A empresa deve comparar, por grupo, indicadores como taxa de aprovação, falsos negativos, falsos positivos, calibração e qualidade das justificativas. Um modelo com 90% de acerto geral ainda pode errar muito mais contra um grupo específico.

## 5. Riscos e impactos

| Risco | Como acontece | Possível consequência | Gravidade |
|---|---|---|---|
| Discriminação indireta | Variáveis substitutas reproduzem gênero, raça ou região | Grupos semelhantes recebem condições diferentes | Alta |
| Erro de dados | Cadastro ou histórico contém informação incorreta | Negação injusta ou juros mais altos | Alta |
| Opacidade | O sistema não apresenta motivo específico | Consumidor não consegue contestar | Alta |
| Automação excessiva | Não existe revisão humana efetiva | Erros são repetidos em grande escala | Alta |
| Vazamento de dados | Muitas informações pessoais são coletadas | Fraude, exposição e perda de privacidade | Alta |
| Exclusão digital | Serviço exige aparelho, internet ou conta digital | Parte da população não consegue solicitar ou recorrer | Média/alta |
| Retroalimentação | Pessoas rejeitadas não geram novos dados positivos | A exclusão atual reforça futuras rejeições | Alta |

## 6. Exclusão digital

A digitalização pode facilitar o acesso ao crédito, mas também criar novas barreiras. Um produto disponível somente em determinado aparelho já limita quem pode participar. Aplicativos pesados, autenticação complexa, falta de acessibilidade e conexão instável prejudicam pessoas com aparelhos antigos ou internet limitada.

O uso de dados alternativos também exige cuidado. Frequência de compras, localização, contatos, tipo de celular e comportamento em aplicativos podem parecer úteis para prever risco, mas podem penalizar pobreza e falta de acesso tecnológico. Uma pessoa com pouco histórico digital não é necessariamente uma pessoa com maior risco financeiro.

Medidas para reduzir a exclusão digital incluem:

- oferecer solicitação e recurso por aplicativo, navegador, telefone e atendimento presencial;
- não reduzir a pontuação somente pela ausência de dados digitais;
- garantir acessibilidade para pessoas com deficiência;
- disponibilizar explicações em linguagem simples;
- permitir correção dos dados e revisão da decisão sem cobrança;
- avaliar separadamente o desempenho do modelo para grupos com pouco histórico.

## 7. Regras propostas de regulamentação e governança

### 7.1 Avaliação de impacto antes do uso

Todo sistema de crédito automatizado deveria passar por uma Avaliação de Impacto Algorítmico antes de entrar em produção. O documento deve informar finalidade, dados usados, grupos afetados, riscos, métricas de equidade, responsáveis e medidas de redução de danos.

### 7.2 Documentação dos dados

A instituição deve manter um inventário com origem, período, qualidade, limitações e representatividade dos dados. Informações sem relação clara com a capacidade de pagamento devem ser excluídas. Dados sensíveis podem ser usados em ambiente controlado para auditoria de equidade, mas não para prejudicar candidatos.

### 7.3 Auditorias independentes

O modelo deve passar por auditoria antes do lançamento e periodicamente. A auditoria deve medir diferenças de aprovação e erro entre grupos, verificar variáveis substitutas e testar mudanças no comportamento dos dados. Resultados relevantes devem ser apresentados ao regulador e resumidos ao público.

### 7.4 Explicação individual

Cada decisão negativa ou condição desfavorável deve trazer motivos específicos e compreensíveis. Expressões genéricas como “política interna” ou “pontuação insuficiente” não ajudam. O consumidor precisa saber quais fatores realmente influenciaram a decisão.

### 7.5 Contestação e revisão

Deve existir um canal gratuito e acessível para corrigir informações e solicitar revisão. A análise humana não pode ser apenas uma repetição automática da nota do sistema. O revisor deve ter autoridade e informações para mudar a decisão quando houver erro ou circunstância relevante.

### 7.6 Monitoramento contínuo

Taxas de aprovação, inadimplência, falsos negativos, reclamações e recursos devem ser acompanhados por grupo e ao longo do tempo. Uma diferença relevante deve gerar investigação, plano de correção e, se necessário, suspensão do modelo.

### 7.7 Responsabilidade definida

O banco continua responsável mesmo quando compra dados ou modelos de outra empresa. Deve haver um responsável executivo pelo sistema, um comitê de risco com participação jurídica e técnica e registro de todas as versões, aprovações e alterações.

### 7.8 Proteção de dados

Devem ser aplicados minimização, finalidade, segurança, retenção limitada e controle de acesso. No Brasil, o artigo 20 da LGPD garante o direito de solicitar revisão de decisões tomadas unicamente com base em tratamento automatizado que afetem interesses, inclusive decisões de perfil de crédito. A lei também prevê informações claras sobre critérios e procedimentos e permite auditoria da autoridade para verificar aspectos discriminatórios.

## 8. Fluxo de governança proposto

1. **Definir a finalidade:** registrar por que o modelo é necessário e quais decisões apoiará.
2. **Avaliar os dados:** verificar qualidade, representatividade, origem e riscos de variáveis substitutas.
3. **Treinar e comparar:** testar modelos simples e complexos, equilibrando desempenho e explicabilidade.
4. **Auditar equidade:** medir resultados e erros por grupo antes da aprovação.
5. **Aprovar com responsáveis:** obter validação técnica, jurídica e de negócio.
6. **Informar o consumidor:** fornecer justificativas claras e canais de recurso.
7. **Monitorar:** acompanhar desempenho, reclamações e mudanças nos dados.
8. **Corrigir ou suspender:** agir quando os limites de risco forem ultrapassados.

## 9. Relação com o laboratório de dados

O arquivo `solicitacoes_credito_simuladas.csv` contém perfis fictícios. Alguns perfis possuem condições financeiras iguais, mas resultados diferentes entre grupos. O notebook calcula:

- quantidade de registros e qualidade da base;
- taxa geral de aprovação;
- taxa de aprovação por gênero simulado;
- taxa de aprovação por região e acesso digital;
- diferença de aprovação entre grupos;
- pares de perfis financeiramente iguais com decisões diferentes.

O objetivo não é provar que o caso Apple Card funcionava dessa forma. A base é uma demonstração didática de como uma equipe de dados pode procurar sinais de tratamento desigual.

## 10. Conclusão

O caso Apple Card mostra que a confiança em uma decisão automatizada depende de mais do que a ausência de uma regra explicitamente discriminatória. A investigação oficial não confirmou violação das leis de crédito, mas identificou falhas de transparência e atendimento e reforçou a necessidade de modernizar a supervisão de modelos de crédito.

Uma governança adequada deve atuar durante todo o ciclo de vida do sistema. Dados precisam ser representativos, variáveis devem ter justificativa, resultados devem ser medidos por grupo, decisões precisam ser explicáveis e consumidores devem ter direito real de contestação. A tecnologia pode ampliar o acesso ao crédito, mas somente quando eficiência e inovação são acompanhadas por responsabilidade, proteção de dados e controle humano.

## Referências

1. NEW YORK STATE DEPARTMENT OF FINANCIAL SERVICES. *Report on Apple Card Investigation*. Março de 2021. Disponível em: <https://www.dfs.ny.gov/reports_and_publications/202103_report_apple_card_investigation>. Acesso em: 18 set. 2026.
2. NEW YORK STATE DEPARTMENT OF FINANCIAL SERVICES. *DFS Issues Findings on the Apple Card and Its Underwriter Goldman Sachs Bank*. 23 mar. 2021. Disponível em: <https://www.dfs.ny.gov/reports_and_publications/press_releases/pr202103231>. Acesso em: 18 set. 2026.
3. BRASIL. *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais*. Disponível em: <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>. Acesso em: 18 set. 2026.
4. CONSUMER FINANCIAL PROTECTION BUREAU. *Circular 2022-03: Adverse action notification requirements in connection with credit decisions based on complex algorithms*. 2022. Disponível em: <https://www.consumerfinance.gov/compliance/circulars/circular-2022-03-adverse-action-notification-requirements-in-connection-with-credit-decisions-based-on-complex-algorithms/>. Acesso em: 18 set. 2026.
5. UNESCO. *Recommendation on the Ethics of Artificial Intelligence*. Disponível em: <https://www.unesco.org/en/artificial-intelligence/recommendation-ethics>. Acesso em: 18 set. 2026.

