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

print(len(df))

print(df[df["preço"] > 1000])

print(df[df["preço"] < 100])