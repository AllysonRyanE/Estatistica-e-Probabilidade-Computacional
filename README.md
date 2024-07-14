<p align="center">
  <img align="center" src='https://user-images.githubusercontent.com/54161035/200095500-d5fec4ba-c97e-4f19-9e39-6764418a736b.png' />
</p>
<p align="center">UNIVERSIDADE FEDERAL DE PERNAMBUCO-UFPE</p>
<p align="center">CENTRO DE INFORMÁTICA</p>

##

<p align="center">
  <img align="center" src='https://img.shields.io/badge/Status-complete-green' />
  <img align="center" src='https://img.shields.io/badge/version-1-green' />
  <img align="center" src='https://img.shields.io/badge/release%20date-abr/2023-green' />
</p>

# Projeto: Análise estatística do uso de RAM para renderização de imagem em VR

## 📕 Resumo

Este projeto teve como objetivo investigar se o desempenho do processador Intel Core i5-10400 seria suficiente para executar o jogo Red Dead Redemption 2. Foram coletados dados de desempenho do CPU durante a execução do jogo e analisados estatisticamente utilizando bibliotecas Python. A normalidade dos dados foi atestada através do gráfico Q-Q e do valor-p, indicando que a base de dados é uma distribuição normal. Foi realizado um Teste Z para verificar se a média de desempenho do CPU seria considerada ideal, resultando na rejeição da hipótese nula. Portanto, concluiu-se que o processador Intel Core i5-10400 não foi eficiente para executar o jogo de interesse.

## 📂 Estrutura do projeto

```
project-statistics-and-probability-computing
├── README.md
├── Relatório Estatística.pdf
├── docs
|  ├── ref_desenvolvimento
|  |  └── fluxo_git.txt
|  └── material_do_projeto
|     ├── Especificação_projeto_2024.1.pdf
|     ├── data_set_group_6_MEMORY.txt
|     └── TEMPLATE_IEEE_LATEX.zip
├── requirements.txt
└── src
   ├── main.ipynb
   └── modules
      ├── Funcao_min_max.py
      ├── __init__.py
      ├── data.py
      ├── graphics.py
      ├── measure_centrality.py
      ├── normal_test.py
      └── setup.py

```

## 🚀 Rodando o projeto

1. Abra o notebook em <span>main.ipynb</span>
2. Execute o Jupyter Notebook
3. Acompanhe os resultados
   Espera-se:
   <img src="./src/assets/teste_de_normalidade.png" />

## 🛠️ Tecnologias utilizadas

- Python 3
- Jupyter Notebook
- NumPy
- SciPy
- Matplotlib
- Seaborn

## 🤝 Autores
Conheça quem faz parte do nosso time

| [<img src="https://avatars.githubusercontent.com/u/115114528?s=400&u=da97e146c53c8b2666a88f74949fc09d5815847c&v=4" width=115><br><sub>Allyson Ryan</sub>](https://github.com/AllysonRyanE) | [<img src="https://avatars.githubusercontent.com/u/80436467?v=4" width=115><br><sub>Jorge Freitas</sub>](https://github.com/jorgelcff) | [<img src="https://avatars.githubusercontent.com/u/94190622?v=4" width=115><br><sub>Lucas Gabriel</sub>](https://github.com/LucasGaab) |
| :--------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------: |
