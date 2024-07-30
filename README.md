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

Este projeto teve como objetivo investigar a otimização do consumo de memória RAM partindo de um processo de renderização de imagem do jogo Minecraft executando em um Apple Vision Pro enquanto o mesmo funcionava como um servidor local. Foram coletados os dados de uso da memória durante a execução e analisados estatisticamente utilizando bibliotecas Python e outras ferramentas. A normalidade dos dados foi atestada através do gráfico Q-Q e do valor-p, indicando que a base de dados é uma distribuição normal. Foi realizado um Teste Z para verificar se a média de uso seria considerada ideal, tendo em perspectiva um limite seguro pré estabelecido e relacionado a segurança para contornar superaquecimentos do dispositivo, resultando na rejeição da hipótese nula. Portanto, concluiu-se que o proceso de renderização de imagem não está otimizado o suficiente para adequar-se aos limites de segurança. 

## 🔗 Link para acesso do Google Colab

#### [Acesse aqui]( https://colab.research.google.com/drive/1SE8oY_u8fuBRA5dFzV2w4n7PvNyYaWeE?usp=sharing)

## 


## 📂 Estrutura do projeto

```
Estatistica-e-Probabilidade-Computacional
├── apresentacao
    └── APRESENTACAO_G6.pdf
├── docs
|  ├── ref_desenvolvimento
|  |  └── fluxo_git.txt
|  └── material_do_projeto
|     ├── Especificação_projeto_2024.1.pdf
|     └── TEMPLATE_IEEE_LATEX.zip
|     ├── data_set_group_6_MEMORY.txt
└── src
   ├── assets
      ├── Boxplot.png
      ├── ConfiabilidadeDaMedia.png
      ├── FluxogramaDaAnalise.png
      .
      .
      .
      └── TesteZ_StatDisk.png
   └── modules
      ├── __init__.py
      ├── critical-z.py
      ├── data.py
      ├── data_set_group_6_MEMORY.txt
      ├── graphics.py
      ├── measure.py
      ├── normal.py
      └── setup.py
   └── requirements.txt
├── LICENSE
├── README.md
├── RELATORIO_FINAL_G6.pdf
      

```

## 🛠️ Principais Tecnologias utilizadas

- Python 3;
- Google Colab;
- NumPy;
- SciPy;
- Matplotlib;
- Seaborn;
- Statdisk Online;
- Minitab

## 🤝 Autores
Conheça quem faz parte do nosso time
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/AllysonRyanE" title="defina o titulo do link">
        <img src="https://avatars.githubusercontent.com/u/115114528?v=4" width="100px;" alt="Foto"/><br>
        <sub>
          <b>Allyson Ryan</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/jorgelcff" title="defina o titulo do link">
        <img src="https://avatars.githubusercontent.com/u/80436467?v=4" width="100px;" alt="Foto"/><br>
        <sub>
          <b>Jorge Freitas</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/LucasGaab" title="defina o titulo do link">
        <img src="https://avatars.githubusercontent.com/u/94190622?v=4" width="100px;" alt="Foto"/><br>
        <sub>
          <b>Lucas Gabriel</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
