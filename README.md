# Projeto Integrador de IA e Governança

**Disciplina:** Ética em Inteligência Artificial  
**Turma:** 3º Ano B — Ensino Médio Técnico  
**Bimestre:** 3º Bimestre  
**Tema:** Algoritmos de crédito e risco de viés — o caso Apple Card/Goldman Sachs

## Equipe Scrum

| Integrante | Papel principal | Responsabilidade |
|---|---|---|
| Kilmes | Scrum Master | Organizar o fluxo, remover impedimentos e acompanhar o WIP |
| Lara | Product Owner | Priorizar o backlog e validar as entregas |
| Antônio | Desenvolvedor de Dados | Criar a base CSV, o notebook e a análise de viés |
| Os Três | Desenvolvedor e QA | Revisar o relatório, testar o notebook e organizar o GitHub |


## Links da entrega

- **Quadro Trello:** https://trello.com/invite/b/6aad19bc0591c27a7866ddd5/ATTIdcbc06bf7c72a418be2702c1cc7962ca8EF15FDD/meu-quadro-do-trello
- **Google Colab:**  https://colab.research.google.com/drive/1yJRSWAPDLwb1pNcnJ2dWKpV1y7yBA3rN?usp=sharing
- **GitHub:** https://github.com/helozx/projeto-ia-governanca-3b

## Estrutura do projeto

```text
projeto_ia_governanca/
├── README.md
├── RELATORIO_IMPACTO_GOVERNANCA.md
├── CHECKLIST_ENTREGA.md
├── ROTEIRO_APRESENTACAO.md
├── CONTRIBUICOES_GITHUB.md
├── dados/
│   └── solicitacoes_credito_simuladas.csv
├── notebook/
│   └── laboratorio_vies_credito.ipynb
├── planejamento/
│   ├── PLANEJAMENTO_AGIL.md
│   └── quadro_kanban.csv
└── evidencias/
    └── README.md
```

## Entregas por pontuação

| Parte | Arquivo principal | Valor |
|---|---|---:|
| Relatório de impacto e governança | `RELATORIO_IMPACTO_GOVERNANCA.md` | 3,0 |
| Scrum, histórias, Planning Poker e Kanban | `planejamento/PLANEJAMENTO_AGIL.md` | 3,0 |
| Laboratório de dados em Python | `notebook/laboratorio_vies_credito.ipynb` | 2,0 |
| Versionamento e participação | `CONTRIBUICOES_GITHUB.md` | 2,0 |

## Como executar o laboratório

1. Abrir o [Google Colab](https://colab.research.google.com/).
2. Selecionar **Arquivo > Fazer upload de notebook**.
3. Enviar `notebook/laboratorio_vies_credito.ipynb`.
4. Executar as células em ordem.
5. Quando solicitado, enviar `dados/solicitacoes_credito_simuladas.csv`.
6. Compartilhar o notebook como **Qualquer pessoa com o link — Leitor**.

## Como publicar no GitHub

Criar um repositório público chamado `projeto-ia-governanca-3b` e enviar todo o conteúdo desta pasta. Cada integrante deve trabalhar na própria branch e realizar os próprios commits. O roteiro completo está em `CONTRIBUICOES_GITHUB.md`.

## Observação sobre a base de dados

A base é totalmente simulada, não contém pessoas reais e foi construída de propósito com decisões desiguais entre grupos. Ela serve apenas para demonstrar como identificar disparidades. Os resultados não devem ser usados para conceder ou negar crédito.

