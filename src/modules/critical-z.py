import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Parâmetros atualizados
z_critical = -1.64485
z_test = -0.530353166378

# Definindo a faixa de valores de z
z_values = np.linspace(-4, 4, 1000)
pdf = stats.norm.pdf(z_values)

# Criando o gráfico
plt.figure(figsize=(10, 6))

# Plot da distribuição normal padrão
plt.plot(z_values, pdf, label="Distribuição Normal Padrão")

# Área de rejeição à esquerda do valor crítico
plt.fill_between(z_values, 0, pdf, where=(z_values <= z_critical), color='red', alpha=0.3, label="Região de Rejeição")

# Linha vertical para o valor crítico
plt.axvline(x=z_critical, color='red', linestyle='--', label=f'Valor Crítico: {z_critical:.5f}')

# Linha vertical para a estatística de teste
plt.axvline(x=z_test, color='blue', linestyle='-', label=f'Estatística de Teste: {z_test:.12f}')

# Labels e título
plt.xlabel('z')
plt.ylabel('Densidade de Probabilidade')
plt.title('Distribuição Normal Padrão e Teste de Hipóteses')
plt.legend()
plt.grid(True)
plt.show()
