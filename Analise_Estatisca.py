import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados do arquivo CSV
df = pd.read_csv('detalles_items_mla.csv')

# Visualizar as primeiras linhas do DataFrame para entender a estrutura dos dados
print(df.head())

# Verificar as dimensões do DataFrame
print(f"Dimensões do DataFrame: {df.shape}")

# Informações gerais sobre o DataFrame
print(df.info())

# Estatísticas descritivas para variáveis numéricas
print(df.describe())

# Histograma da distribuição de preços
plt.figure(figsize=(10, 6))
sns.histplot(df['Preco'], bins=20, kde=True)
plt.title('Distribuição de Preços')
plt.xlabel('Preço')
plt.ylabel('Contagem')
plt.show()

# Contagem de produtos por condição
plt.figure(figsize=(8, 5))
sns.countplot(x='Condicao', data=df)
plt.title('Contagem de Produtos por Condição')
plt.xlabel('Condição')
plt.ylabel('Contagem')
plt.show()

# Matriz de correlação entre as variáveis numéricas
df_numeric = df.select_dtypes(include=['int64', 'float64'])
corr_matrix = df_numeric.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Matriz de Correlação')
plt.show()

# Scatter plot de preço versus quantidade vendida
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Preco', y='Condicao', data=df)
plt.title('Preço vs. Condição Item')
plt.xlabel('Preço')
plt.ylabel('Quantidade Vendida')
plt.show()