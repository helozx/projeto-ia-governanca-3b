# Plano de versionamento e participação no GitHub

## Regra principal

Os commits precisam ser feitos pelas contas reais dos integrantes. Não criem commits fingindo ser outra pessoa. O professor poderá conferir autor, data, branch e alterações.

## Branches

| Branch | Integrante | Conteúdo |
|---|---|---|
| `main` | Equipe | Versão aprovada e pronta para entrega |
| `docs/relatorio-lara` | Lara | Caso real, falhas e referências |
| `chore/kanban-kilmes` | Kilmes | Scrum, Kanban, WIP e checklist |
| `feat/dados-antonio` | Antônio | Base CSV e dicionário dos dados |
| `feat/notebook-antonio` | Antônio | Notebook do Colab |
| `docs/revisao-integrante4` | **[4º INTEGRANTE]** | Revisão, testes e evidências |

## Sequência recomendada de commits

| Ordem | Autor real | Mensagem sugerida |
|---:|---|---|
| 1 | Kilmes | `chore: cria estrutura inicial do projeto` |
| 2 | Lara | `docs: adiciona contexto do caso Apple Card` |
| 3 | Lara | `docs: analisa riscos e propostas de governanca` |
| 4 | Kilmes | `docs: define papeis e eventos scrum` |
| 5 | Kilmes | `docs: adiciona kanban e limites de wip` |
| 6 | Antônio | `data: adiciona base simulada de credito` |
| 7 | Antônio | `feat: importa e valida csv no notebook` |
| 8 | Antônio | `feat: calcula indicadores de disparidade` |
| 9 | **[4º INTEGRANTE]** | `test: executa notebook e registra validacao` |
| 10 | **[4º INTEGRANTE]** | `docs: revisa nomes links e referencias` |
| 11 | Lara | `docs: ajusta relatorio apos revisao` |
| 12 | Kilmes | `chore: finaliza checklist de entrega` |

## Fluxo de colaboração

1. Clonar o repositório.
2. Cada integrante criar sua branch.
3. Alterar somente os arquivos de sua responsabilidade.
4. Fazer commits pequenos com mensagens claras.
5. Enviar a branch para o GitHub.
6. Abrir Pull Request para `main`.
7. Outro integrante revisar e aprovar.
8. Fazer merge preservando o histórico.

## Comandos básicos

```bash
git clone URL_DO_REPOSITORIO
cd projeto-ia-governanca-3b
git switch -c docs/relatorio-lara
git add RELATORIO_IMPACTO_GOVERNANCA.md
git commit -m "docs: adiciona contexto do caso Apple Card"
git push -u origin docs/relatorio-lara
```

Cada integrante deve configurar o próprio nome e e-mail antes de realizar commits:

```bash
git config user.name "NOME REAL"
git config user.email "EMAIL_DA_CONTA_GITHUB"
```

## Evidências para salvar

Adicionar na pasta `evidencias/`:

- captura da tela **Insights > Contributors**;
- captura dos Pull Requests aprovados;
- captura do histórico de commits;
- captura do quadro Trello;
- arquivo ou captura da execução completa do Colab.

## Critérios de aceitação do repositório

- repositório público e acessível sem login;
- README aparece na página inicial;
- arquivos abrem sem erro;
- notebook está dentro da pasta `notebook/`;
- dados estão dentro da pasta `dados/`;
- cada membro possui pelo menos dois commits reais;
- nenhuma senha, token ou dado pessoal foi publicado;
- link do Colab e do Trello foi inserido no README.

