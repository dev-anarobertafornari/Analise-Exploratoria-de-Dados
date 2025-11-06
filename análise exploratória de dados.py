# -*- coding: utf-8 -*-
"""
Autora: Ana Roberta Fornari  24/10/2025
"""

# Bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# URL do CSV do Titanic
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

df.head()

# Verifica valores nulos
df.isnull().sum()

#Gráfico de barras
sns.heatmap(df.isnull(), cbar=False, yticklabels=False, cmap='viridis')
plt.show()

df.describe()

df.describe(include=['O'])

# Ver as colunas quantitativas e quais são categóricas.
df.dtypes

quantitativas = df.select_dtypes(include=[np.number]).columns.tolist()
categoricas = df.select_dtypes(include=['object']).columns.tolist()

print("Colunas quantitativas:", quantitativas)
print("Colunas categóricas:", categoricas)

for col in quantitativas:
    plt.figure(figsize=(8,4))
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot de {col}')
    plt.show()

# Analisa a correlação entre as variáveis numéricas
numericas = df.select_dtypes(include=[np.number])

corr = numericas.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()

"""Aqui começa os diagramas
"""

# Histograma
df['Age'].hist(bins=20)
plt.title('Distribuição das Idades')
plt.xlabel('Idade')
plt.ylabel('Contagem')
plt.show()

# Gráfico de Linha
df.groupby('Pclass')['Survived'].mean().plot(kind='line', marker='o')
plt.title('Taxa de Sobrevivência por Classe')
plt.ylabel('Sobrevivência média')
plt.show()

# Gráfico de Dispersão
sns.scatterplot(x='Age', y='Fare', hue='Survived', data=df)
plt.title('Idade x Tarifa por Sobrevivência')
plt.show()

"""Respondendo as questões"""

# Calcula a taxa média de sobrevivência por sexo
df.groupby('Sex')['Survived'].mean()

bins = [0, 18, 60, 100]
labels = ['0-18', '19-60', '61-100']

df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels)

df.groupby('AgeGroup')['Survived'].mean()

sns.barplot(x='Pclass', y='Survived', data=df)
plt.title('Sobrevivência por Classe')
plt.show()

from sklearn.model_selection import train_test_split

X = df.drop('Survived', axis=1)
y = df['Survived']

from sklearn.model_selection import train_test_split
3
X = df.drop('Survived', axis=1)
y = df['Survived']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Verificando os tamanhos dos conjuntos
print("Tamanho X_train:", X_train.shape)
print("Tamanho X_test:", X_test.shape)
print("Tamanho y_train:", y_train.shape)
print("Tamanho y_test:", y_test.shape)
