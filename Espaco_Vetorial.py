# Importando os pacotes

import collections
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import wb

# Vetor de 1 linha com 3 colunas
vetor1 = np.array([1, 2, 3])
print(vetor1)

# Vetor de 3 linhas com 1 coluna
vetor2 = np.array([[1], [2], [3]])
print(vetor2)

# Geometria de Vetores e Representação em Python
u = np.array([-2, 3])
print(u)

# Criando figura
plt.figure(figsize = (5, 5))

# Vetor u
vetor_imagem = plt.arrow(0,
                        0,
                        u[0],
                        u[1],
                        head_width = .3,
                        width = .1,
                        color = 'blue',
                        length_includes_head = True)

# Ponto (0, 0)
plt.plot(0, 0, 'ko', markerfacecolor = 'yellow', markersize = 8)

# Formação do Plot
plt.grid(linestyle = '--', alpha = .6)
plt.axis('square')
plt.axis([-4, 4, -4, 4])
plt.legend([vetor_imagem], ['u'])
plt.title('Vetor no Plano Cartesiano')
plt.savefig('grafico_01.png')
plt.show()

# Efeito de valores escalares no vetor

valores_escalares = [1, 2, 1/2, -1, -2]

vetor_inicial = np.array([ .9, 1.2])

# Criando figura
fig, axs = plt.subplots(1, len(valores_escalares), figsize = (14, 5))

# Loop
i = 0

for valor in valores_escalares:
    
    vetor_resultante = valor * vetor_inicial

    # Plot do vetor inicial
    axs[i].arrow(
        0,
        0,
        vetor_inicial[0],
        vetor_inicial[1],
        head_width = .3,
        width = .1,
        color = 'blue',
        length_includes_head = True
    )

    # Plot do vetor resultante
    axs[i].arrow(
        0.1,
        0,
        vetor_resultante[0],
        vetor_resultante[1],
        head_width = .3,
        width = .1,
        color = 'red',
        length_includes_head = True
    )

    # Grid
    axs[i].grid(linestyle = '--')

    # Formato
    axs[i].axis('square')

    # Eixos
    axs[i].axis([-2.5, 2.5, -2.5, 2.5])

    # Limites
    axs[i].set(xticks = np.arange(-2, 3), yticks = np.arange(-2, 3))

    # Título
    axs[i].set_title(f'$\sigma$ = {valor:.2f}')

    # Contador
    i += 1

plt.tight_layout()
plt.savefig('grafico_02.png')
plt.show()
