# 🐼 Estudos de Python com Pandas

Este repositório reúne meus primeiros estudos e exercícios com a biblioteca Pandas, como parte da minha evolução nos estudos de Python para Dados.

## 📚 O que estou estudando

Neste primeiro exercício, pratiquei:

- Importação da biblioteca Pandas
- Criação de dados com dicionários
- Criação de um DataFrame
- Seleção de colunas
- Cálculo de média
- Identificação do maior e menor valor
- Soma de valores
- Contagem de registros
- Filtros utilizando condições

## 💻 Exemplo

```python
import pandas as pd

dados = {
    "Nome": ["Notebook", "Mouse", "PC"],
    "preço": [1200, 40, 4500],
    "Categoria": ["informatica", "informatica", "informatica"]
}

df = pd.DataFrame(dados)

print(df)

print(df["preço"].mean())
print(df["preço"].max())
print(df["preço"].sum())
print(df["preço"].min())

print(df[df["preço"] > 1000])
print(df[df["preço"] < 100])
