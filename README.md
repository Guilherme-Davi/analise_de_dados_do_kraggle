# Link da atividade pelo GOOGLE COLAB:
https://colab.research.google.com/drive/13Sl9cmAJGjV54qB6lum5laqsFIutLw94?usp=sharing
# Atenção, a atividade publicada aqui no github está pronta para ser executada no VS CODE, caso queira olhar pelo colab, clicar no link acima!

# analise_de_dados_do_kraggle
Objetivo: Nesta atividade, você vai aplicar um fluxo de trabalho completo de análise de
dados — da aquisição à visualização — usando um dataset de sua escolha(utilizei "Video Game Sales"). 
Isso o ajudará a desenvolver a capacidade de adaptação, uma habilidade crucial para qualquer analista.

# Visualização principal:
O gráfico mostra que gêneros como Platform e Shooter apresentam,
em média, as maiores vendas globais por jogo. Já gêneros como Adventure e Strategy
possuem valores médios bem menores, indicando que atraem nichos mais específicos.

# Visualização de relação:
O gráfico de dispersão mostra que há uma tendência positiva: quando um jogo
vende mais na América do Norte, geralmente também apresenta boas vendas no
resto do mundo. Porém, há pontos isolados que fogem da tendência, indicando
jogos que tiveram sucesso mais localizado.


# INSTRUÇÕES DA ATIVIDADE:
Requisitos do Dataset (Escolha um que atenda a estes critérios):
Disponibilidade: Deve ser um arquivo CSV acessível (pode ser do Kaggle, de alguma base de dados pública ou de sua autoria).
Mínimo de 3 Colunas: O dataset precisa ter pelo menos 3 colunas que permitam uma análise interessante.
Dados Numéricos e Categóricos: Deve conter pelo menos uma coluna com dados numéricos (ex: preço, vendas, idade) e pelo menos uma com dados categóricos (ex: gênero, país, categoria de produto).
Adequado para Merge: O ideal é que você possa encontrar um segundo dataset (relacionado) com pelo menos uma coluna em comum para a prática do merge. Se não for possível, você pode simular a criação de um segundo DataFrame.

Exemplos de Datasets do Kaggle que funcionam bem:
"Video Game Sales" < UTILIZADO POR MIM
"Netflix Movies and TV Shows"
"COVID-19 in Brazil"
"House Prices"

Preparação:
Escolha e baixe seu dataset: Vá ao Kaggle ou a outra fonte de dados, escolha o arquivo CSV e faça o download.
Coloque o arquivo no seu ambiente de trabalho: Salve o arquivo na mesma pasta do seu Jupyter Notebook ou faça o upload para o Google Colab.

Python
# Importar bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações para melhor visualização dos gráficos
plt.style.use('seaborn-v0_8-darkgrid') 
sns.set_palette('viridis') 
 

# Parte 1: Leitura e Seleção de Dados Iniciais

Leia o arquivo CSV:
Carregue seu arquivo .csv em um DataFrame. Lembre-se de substituir "nome_do_seu_arquivo.csv" pelo nome real do seu arquivo.
Use df.head() e df.info() para ter uma visão geral dos dados.

Selecione colunas relevantes:
Escolha pelo menos 4 colunas que você acha interessantes para a sua análise.
Crie um novo DataFrame com essas colunas selecionadas.

# Parte 2: Fusão de DataFrames e Criação de Novas Colunas

Crie um DataFrame secundário para o merge:
Cenário 1 (Recomendado): Se você tiver um segundo arquivo CSV relacionado, leia-o e prepare-o para o merge.
Cenário 2 (Alternativa): Se não tiver um segundo arquivo, crie um DataFrame simples. Por exemplo, se seu dataset principal tem uma coluna País, você pode criar um pequeno DataFrame com País e uma nova coluna Continente para fazer o merge.
Certifique-se de que os dois DataFrames tenham pelo menos uma coluna em comum para a junção.

Realize o Merge:
Faça o merge entre seu DataFrame principal e o secundário usando a(s) coluna(s) em comum.
Armazene o resultado em um novo DataFrame e exiba as primeiras linhas para verificar se a junção foi bem-sucedida.

Crie uma Coluna de Análise:
Use duas colunas numéricas do seu DataFrame para criar uma nova coluna. Por exemplo:
lucro = receita - custo
densidade_populacional = populacao / area
media_por_item = valor_total / quantidade

# Parte 3: Análise e Visualização de Dados
 
Agrupe e analise seus dados:
Escolha uma coluna categórica (ex: País, Gênero, Categoria) e agrupe o DataFrame por ela.
Calcule a média de uma coluna numérica relevante (ex: lucro, vendas).
Ordene o resultado do maior para o menor.

Crie a Visualização Principal:
Use o DataFrame resultante do agrupamento para criar um gráfico de barras.
O eixo X deve representar a coluna categórica (agrupamento).
O eixo Y deve representar a média que você calculou.
Certifique-se de adicionar um título claro, rótulos nos eixos e interpretar o que o gráfico está mostrando.

Crie a Visualização de Relação:
Escolha duas colunas numéricas do seu DataFrame.
Crie um gráfico de dispersão (scatterplot) para visualizar a relação entre elas.
Tente identificar se há uma correlação. Por exemplo: países com maior população têm um número maior de casos de COVID-19?
