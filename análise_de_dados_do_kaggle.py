import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette('viridis')

# Carregar dados de vendas
df = pd.read_csv("vgsales.csv")
print("\nInformações do vgsales.csv:")
df.info()
print("\nPrimeiras linhas do vgsales.csv:")
print(df.head(30))

colunas_relevantes = ["Rank", "Name", "Platform", "Year", "Genre", "Publisher", "NA_Sales", "Global_Sales"]
df_relevantes = df[colunas_relevantes]
print("\nPrimeiras linhas das colunas relevantes:")
print(df_relevantes.head(30))

# Carregar dados de fabricantes
df_fabricante = pd.read_csv("platforms_manufacturer.csv")
print("\nInformações do platforms_manufacturer.csv:")
df_fabricante.info()
print("\nPrimeiras linhas do platforms_manufacturer.csv:")
print(df_fabricante.head(30))

# Unir os DataFrames
df_juntos = pd.merge(df_relevantes, df_fabricante, on="Platform")
print("\nInformações do DataFrame unido:")
df_juntos.info()
print("\nPrimeiras linhas do DataFrame unido:")
print(df_juntos.head(30))

# Calcular vendas globais sem América do Norte
df_juntos["Global_without_NA"] = df_juntos["Global_Sales"] - df_juntos["NA_Sales"]
print("\nPrimeiras linhas com coluna Global_without_NA:")
print(df_juntos.head(30))

# Média de vendas globais por gênero
df_genero = (
    df_juntos.groupby("Genre")["Global_Sales"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)
print("\nMédia de vendas globais por gênero:")
print(df_genero.head(30))

# Gráfico de barras: média de vendas globais por gênero
plt.figure(figsize=(10,6))
plt.bar(df_genero["Genre"], df_genero["Global_Sales"])
plt.title("Média de Vendas Globais por Gênero")
plt.xlabel("Gênero")
plt.ylabel("Vendas Globais Médias (em milhões)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# O gráfico mostra que gêneros como Platform e Shooter apresentam,
# em média, as maiores vendas globais por jogo. Já gêneros como Adventure e Strategy
# possuem valores médios bem menores, indicando que atraem nichos mais específicos.

# Gráfico de dispersão: relação entre vendas NA e no resto do mundo
plt.figure(figsize=(10,6))
plt.scatter(df_juntos["NA_Sales"], df_juntos["Global_without_NA"])
plt.title("Relação entre Vendas na América do Norte e no Resto do Mundo")
plt.xlabel("Vendas NA (em milhões)")
plt.ylabel("Global sem NA (em milhões)")
plt.tight_layout()
plt.show()

# O gráfico de dispersão mostra que há uma tendência positiva: quando um jogo
# vende mais na América do Norte, geralmente também apresenta boas vendas no
# resto do mundo. Porém, há pontos isolados que fogem da tendência, indicando
# jogos que tiveram sucesso mais localizado.
