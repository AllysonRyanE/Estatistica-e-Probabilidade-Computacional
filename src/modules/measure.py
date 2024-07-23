"""Esse módulo contém as medidas de centralidade e de dispersão relevantes"""

from scipy.stats import kurtosis, skew
from graphics import df

def measures(data):
    """
    Cria as medidas descritivas
    Arg:
        data: Dados formatados
    Return:
        Dicionário contendo várias medidas
    """
    # Calculando as estatísticas descritivas
    mean = data.mean() #Média
    median = data.median() #Mediana
    std_dev = data.std() #Desvio padrão
    variance = data.var() #Variância
    coef_var = (std_dev / mean) * 100
    quartiles = data.quantile([0.25, 0.5, 0.75, 1]) #1º- 4º quartil
    min_value = data.min() #Valor minimo
    max_value = data.max() #Valor máximo
    kurt = kurtosis(data) #Curtose
    skewness = skew(data) #Assimetria de Fisher
    iqr = quartiles[0.75] - quartiles[0.25] #IQR

    # Calculando os outliers usando o IQR
    lower_bound = quartiles[0.25] - 1.5 * iqr
    upper_bound = quartiles[0.75] + 1.5 * iqr
    outliers = data[(data < lower_bound) | (data > upper_bound)]

    measures = {
        "mean": mean,
        "median": median,
        "std_dev": std_dev,
        "variance": variance,
        "coef_var": coef_var,
        "quartiles": quartiles.tolist(),
        "min_value": min_value,
        "max_value": max_value,
        "iqr": iqr,
        "kurtosis": kurt,
        "skewness": skewness,
        "lower_bound": lower_bound,
        "upper_bound": upper_bound,
        "outliers_count": len(outliers)
    }
    return measures

print(measures(df["Memory_Usage_MB"]))