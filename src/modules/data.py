"""Esse módulo formata os dados"""

def read_data(path):
    """
    Lê o arquivo .txt com os dados
    Arg:
        path: endereço do arquivo.
    Return:
        Uma variável com o arquivo aberto em modo leitura.
    """
    data_set = open(path, 'r')
    return data_set


def format(path):
    """
    Formatar arquivo .txt que contém os dados
    Arg:
        path: endereço do arquivo.
    Return:
        Uma lista com dados formatados e no tipo float.
    """
    data = []
    data_set = read_data(path)
    for linha in data_set:
        data.append(float(linha.replace(',', '.')))
    return data

data = format('data_set_group_6_MEMORY.txt')
for i in data:
    print(i)
#Faça uma chamada similar a esta para executar as funções acima corretamente armazenando a lista retornada da função 'format' (Obs: Atente-se ao local do arquivo informado).