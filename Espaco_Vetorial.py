# Importando os pacotes

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