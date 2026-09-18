import json
import sys
from pathlib import Path


def markdown(source):
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in source.strip().split("\n")],
    }


def code(source):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in source.strip().split("\n")],
    }


cells = [
    markdown(
        """
# Laboratório de Dados — Viés em Algoritmos de Crédito

**Disciplina:** Ética em Inteligência Artificial  
**Turma:** 3º Ano B — Ensino Médio Técnico  
**Equipe:** Kilmes, Lara, Antônio e **[NOME DO 4º INTEGRANTE]**

Este notebook analisa uma base **totalmente simulada**. Nenhuma linha representa uma pessoa real. A desigualdade foi inserida propositalmente para demonstrar técnicas simples de auditoria. Os resultados não podem ser usados para avaliar crédito real.
"""
    ),
    markdown(
        """
## 1. Objetivos

1. Importar e ler um arquivo CSV.
2. Conferir a qualidade básica dos dados.
3. Calcular taxas de aprovação por grupo.
4. Visualizar diferenças de resultado.
5. Procurar perfis financeiros iguais que receberam decisões diferentes.
6. Discutir limites da análise e medidas de governança.
"""
    ),
    code(
        """
import os
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
plt.style.use("seaborn-v0_8-whitegrid")
"""
    ),
    markdown(
        """
## 2. Carregamento do arquivo

No Google Colab será aberta uma caixa para enviar `solicitacoes_credito_simuladas.csv`. Em execução local, o código procura o arquivo dentro da pasta do projeto.
"""
    ),
    code(
        """
arquivo = None

try:
    from google.colab import files
    enviados = files.upload()
    if enviados:
        arquivo = next(iter(enviados))
except ImportError:
    candidatos = [
        "dados/solicitacoes_credito_simuladas.csv",
        "../dados/solicitacoes_credito_simuladas.csv",
        "/content/solicitacoes_credito_simuladas.csv",
    ]
    arquivo = next((c for c in candidatos if os.path.exists(c)), None)

if arquivo is None:
    raise FileNotFoundError(
        "Arquivo não encontrado. Envie solicitacoes_credito_simuladas.csv."
    )

df = pd.read_csv(arquivo)
print(f"Arquivo carregado: {arquivo}")
print(f"Linhas: {df.shape[0]} | Colunas: {df.shape[1]}")
df.head()
"""
    ),
    markdown(
        """
## 3. Dicionário dos dados

| Coluna | Significado |
|---|---|
| `id_solicitacao` | Identificador fictício |
| `renda_mensal` | Renda mensal simulada |
| `divida_total` | Dívida total simulada |
| `tempo_emprego_meses` | Tempo de emprego em meses |
| `idade` | Idade fictícia |
| `genero_simulado` | Grupo M ou F criado para auditoria didática |
| `regiao_simulada` | Região Central ou Periférica |
| `acesso_digital` | Acesso Completo ou Limitado |
| `score_credito` | Pontuação financeira simulada |
| `pontuacao_modelo` | Nota produzida pela regra simulada |
| `resultado` | 1 para aprovado e 0 para negado |
| `decisao` | Resultado em texto |
| `motivo_informado` | Justificativa mostrada ao candidato |
"""
    ),
    code(
        """
print("Tipos de dados:")
display(df.dtypes.to_frame("tipo"))

qualidade = pd.DataFrame({
    "nulos": df.isna().sum(),
    "valores_unicos": df.nunique(),
})
display(qualidade)

print("Linhas duplicadas:", int(df.duplicated().sum()))
assert df.shape[0] >= 40, "A base deveria possuir pelo menos 40 registros."
assert df["id_solicitacao"].is_unique, "Os identificadores precisam ser únicos."
assert df.isna().sum().sum() == 0, "Existem valores nulos na base."
assert set(df["resultado"].unique()).issubset({0, 1})
print("Validações concluídas sem erro.")
"""
    ),
    markdown(
        """
## 4. Visão geral

A média da coluna `resultado` representa a taxa de aprovação, pois aprovado vale 1 e negado vale 0.
"""
    ),
    code(
        """
taxa_geral = df["resultado"].mean()
resumo = pd.DataFrame({
    "indicador": ["Solicitações", "Aprovadas", "Negadas", "Taxa de aprovação"],
    "valor": [
        len(df),
        int(df["resultado"].sum()),
        int((1 - df["resultado"]).sum()),
        f"{taxa_geral:.1%}",
    ],
})
display(resumo)
"""
    ),
    markdown(
        """
## 5. Taxa de aprovação por grupo

Uma diferença de taxa é um **sinal de auditoria**, não uma prova isolada de discriminação. É necessário comparar perfis, verificar erros, entender o processo e analisar contexto e legislação.
"""
    ),
    code(
        """
def taxa_por_grupo(coluna):
    tabela = (
        df.groupby(coluna, as_index=False)
        .agg(solicitacoes=("resultado", "size"), aprovadas=("resultado", "sum"))
    )
    tabela["taxa_aprovacao"] = tabela["aprovadas"] / tabela["solicitacoes"]
    return tabela.sort_values("taxa_aprovacao", ascending=False)

por_genero = taxa_por_grupo("genero_simulado")
por_regiao = taxa_por_grupo("regiao_simulada")
por_acesso = taxa_por_grupo("acesso_digital")

def exibir_percentual(tabela):
    exibicao = tabela.copy()
    exibicao["taxa_aprovacao"] = exibicao["taxa_aprovacao"].map(lambda x: f"{x:.1%}")
    display(exibicao)

print("Por gênero simulado")
exibir_percentual(por_genero)
print("Por região simulada")
exibir_percentual(por_regiao)
print("Por acesso digital")
exibir_percentual(por_acesso)
"""
    ),
    code(
        """
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

for ax, tabela, coluna, titulo in [
    (axes[0], por_genero, "genero_simulado", "Por gênero simulado"),
    (axes[1], por_regiao, "regiao_simulada", "Por região"),
    (axes[2], por_acesso, "acesso_digital", "Por acesso digital"),
]:
    ax.bar(tabela[coluna], tabela["taxa_aprovacao"], color="#2F75B5")
    ax.set_ylim(0, 1)
    ax.set_title(titulo)
    ax.set_ylabel("Taxa de aprovação")
    ax.yaxis.set_major_formatter(lambda x, pos: f"{x:.0%}")
    for i, valor in enumerate(tabela["taxa_aprovacao"]):
        ax.text(i, valor + 0.03, f"{valor:.1%}", ha="center")

plt.tight_layout()
plt.show()
"""
    ),
    markdown(
        """
## 6. Métricas simples de disparidade

- **Diferença de aprovação:** taxa do grupo M menos taxa do grupo F.
- **Razão de impacto:** taxa do grupo F dividida pela taxa do grupo M.

Essas medidas ajudam a localizar um problema, mas não substituem auditoria completa, análise jurídica ou investigação das causas.
"""
    ),
    code(
        """
taxas_genero = df.groupby("genero_simulado")["resultado"].mean()
taxa_m = taxas_genero.get("M", float("nan"))
taxa_f = taxas_genero.get("F", float("nan"))
diferenca_pp = (taxa_m - taxa_f) * 100
razao_impacto = taxa_f / taxa_m if taxa_m > 0 else float("nan")

metricas = pd.DataFrame({
    "metrica": [
        "Taxa grupo M",
        "Taxa grupo F",
        "Diferença M - F",
        "Razão F / M",
    ],
    "resultado": [
        f"{taxa_m:.1%}",
        f"{taxa_f:.1%}",
        f"{diferenca_pp:.1f} pontos percentuais",
        f"{razao_impacto:.2f}",
    ],
})
display(metricas)
"""
    ),
    markdown(
        """
## 7. Comparação de perfis financeiros iguais

A base foi construída em pares. Pessoas fictícias de grupos diferentes possuem renda, dívida, emprego, idade, região, acesso digital e score iguais. Se o resultado variar dentro do par, existe uma evidência direta de tratamento diferente na regra simulada.
"""
    ),
    code(
        """
chaves_perfil = [
    "renda_mensal",
    "divida_total",
    "tempo_emprego_meses",
    "idade",
    "regiao_simulada",
    "acesso_digital",
    "score_credito",
]

perfis_divergentes = (
    df.groupby(chaves_perfil, as_index=False)
    .agg(
        quantidade=("id_solicitacao", "size"),
        resultados_diferentes=("resultado", "nunique"),
    )
    .query("quantidade > 1 and resultados_diferentes > 1")
)

detalhes_divergentes = df.merge(perfis_divergentes[chaves_perfil], on=chaves_perfil)
detalhes_divergentes = detalhes_divergentes.sort_values(chaves_perfil + ["genero_simulado"])

print("Perfis idênticos com decisões divergentes:", len(perfis_divergentes))
display(
    detalhes_divergentes[
        ["id_solicitacao", "genero_simulado", "score_credito", "pontuacao_modelo", "decisao"]
    ].head(20)
)
"""
    ),
    markdown(
        """
## 8. Conclusão da auditoria

A base simulada apresentou diferença de aprovação entre os grupos M e F e também contém pares financeiramente iguais com decisões diferentes. Isso ocorre porque a regra artificial aplicada na criação do arquivo inseriu uma penalidade oculta para o grupo F, além de penalidades por região periférica e acesso digital limitado.

Em um sistema real, a equipe deveria:

1. suspender o uso do modelo em decisões de alto impacto até entender a causa;
2. remover ou justificar variáveis sem relação legítima com capacidade de pagamento;
3. testar desempenho e erros por grupo;
4. corrigir dados e reavaliar candidatos prejudicados;
5. fornecer motivos específicos e canal de contestação;
6. registrar versões, responsáveis e resultados das auditorias;
7. monitorar o modelo continuamente.

**Limite do experimento:** os dados são pequenos, artificiais e foram criados para mostrar um problema. A análise não descreve clientes reais nem reproduz o modelo usado no caso Apple Card.
"""
    ),
]

notebook = {
    "cells": cells,
    "metadata": {
        "colab": {"name": "laboratorio_vies_credito.ipynb", "provenance": []},
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3",
        },
        "language_info": {"name": "python", "version": "3"},
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}

output = Path(sys.argv[1])
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(notebook, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(output)
