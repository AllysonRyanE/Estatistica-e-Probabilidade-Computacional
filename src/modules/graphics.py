import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from data import data

# Convertendo a lista importado do 'data.py' em um DataFrame para facilitar a manipulação
df = pd.DataFrame(data, columns=["Memory_Usage_MB"])
# Configurações de estilo para os gráficos que serão gerados
sns.set(style="whitegrid")

# Boxplot da utilização de memória
def boxplot(data):
    """
    Cria o gráfico boxplot
    Arg:
        data: Dados formatados
    Return:
        Criação gráfica do boxplot a partir dos dados inseridos
    """
    plt.figure(figsize=(12, 12))
    sns.boxplot(x=data, color='green')
    # Definindo o título e rótulos dos eixos
    plt.title("Boxplot da Utilização de Memória (MB)", fontsize=22)
    plt.xlabel("Utilização de Memória (MB)", fontsize=18)
    # Aumentando o tamanho da fonte dos valores dos eixos
    plt.tick_params(axis='x', labelsize=18)
    plt.tick_params(axis='y', labelsize=18)

    return plt.show()

# Histograma da utilização de memória
def histograma(data):
    """
    Cria o gráfico histograma
    Arg:
        data: Dados formatados
    Return:
        Criação gráfica em histograma a partir dos dados inseridos
    """
    plt.figure(figsize=(12, 12))
    sns.histplot(data, bins=30, kde=True, color='blue')
    # Definindo o título e rótulos dos eixos
    plt.title("Distribuição da Utilização de Memória (MB)", fontsize=22)
    plt.xlabel("Utilização de Memória (MB)", fontsize=18)
    plt.ylabel("Frequência", fontsize=18)
    # Aumentando o tamanho da fonte dos valores dos eixos
    plt.tick_params(axis='x', labelsize=18)
    plt.tick_params(axis='y', labelsize=18)

    return plt.show()

# Gráfico de Linha da utilização de memória
def linechart(data):
    """
    Cria o gráfico de linha
    Arg:
        data: Dados formatados
    Return:
        Criação gráfica do gráfico de linha a partir dos dados inseridos
    """
    plt.figure(figsize=(12, 12))
    plt.plot(data, color='purple')
    # Definindo o título e rótulos dos eixos
    plt.title("Utilização de Memória ao Longo do Tempo", fontsize=22)
    plt.xlabel("Amostra", fontsize=18)
    plt.ylabel("Utilização de Memória (MB)", fontsize=18)
    # Aumentando o tamanho da fonte dos valores dos eixos
    plt.tick_params(axis='x', labelsize=18)
    plt.tick_params(axis='y', labelsize=18)

    return plt.show()


# Chamando as funções para visualizar as alterações
#boxplot(df["Memory_Usage_MB"])
#histograma(df["Memory_Usage_MB"])
#linechart(df["Memory_Usage_MB"])
