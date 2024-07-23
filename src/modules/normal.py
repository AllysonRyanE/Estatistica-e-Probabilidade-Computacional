"""Esse módulo contém as funções para certificar-se que segue uma distribuição normal"""


import matplotlib.pyplot as plt
from scipy.stats import normaltest, probplot
from graphics import df, sns

def pvalor(data):
    """
    Calcula o p-value dos dados
    Arg:
        data: dados formatados e em dataframe.
    Return:
        Um número real representando o valor do p-valor.
    """
    stat, p = normaltest(data)
    return stat, p


def grafico_qq(data):
    """
    Cria um Q-Q plot para um conjunto de dados.
    
    Args:
        data: conjunto de dados formatados e em dataframe a ser plotado.
    Return:
        Plotagem de quantis teóricos contra os quantis reais dos dados.
    """
    fig, ax = plt.subplots(figsize=(12, 12))
    probplot(data, plot=ax)

    # Definir título e rótulos dos eixos
    ax.set_title("Gráfico Q-Q da utilização de memória pelo processo", fontsize= '22')
    ax.set_xlabel("Quantis teóricos", fontsize='18')
    ax.set_ylabel("Quantis observados", fontsize='18')
    # Aumentando o tamanho da fonte dos valores dos eixos
    ax.tick_params(axis='x', labelsize=18)
    ax.tick_params(axis='y', labelsize=18)
    return plt.show()

#grafico_qq(df["Memory_Usage_MB"])
print(pvalor(df["Memory_Usage_MB"]))
