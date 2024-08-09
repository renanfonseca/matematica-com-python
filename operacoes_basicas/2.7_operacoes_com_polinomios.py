# OPERAÇÕES COM POLINÔMIOS

# Operações com polinômios podem ser feitas importanto algumas funções da 
# biblioteca numpy 

import numpy as np
import matplotlib.pyplot as plt


# numpy trabalha os polinômios definidos por vetorescom os valores de seus 
# coeficientes. Exemplo, o polinômio 2x^2+4x-2 seria representado pelo vetor
# [2, 4, -2] 

polinomio_1 = [2, 4, -2]
polinomio_2 = [1, -1, -3]

# Outra forma de representar polinômios é usando a função poly1d([2, 4, -2])

polinomio_1_poly1d = np.poly1d([2, 4, -2])
polinomio_2_poly1d = np.poly1d([1, -1, -3])
polinomio_3_poly1d = np.poly1d([1, -2, -5, 6])

print(f'Usando a função poly1d() - np.poly1d([2, 4, -2]) = '
      f'\n{polinomio_1_poly1d}\n')

print(f'Usando a função poly1d() - np.poly1d([1, -1, -3]) '
      f'\n{polinomio_2_poly1d}\n')

print(f'Usando a função poly1d() - np.poly1d([3, 1, -1, -3]) '
      f'\n{polinomio_3_poly1d}\n')

print(f'Com isso podemos achar as raizes usando polinomio_x_poly1d.roots'
      f'\n polinomio_1_poly1d.root = {polinomio_1_poly1d.roots}'
      f'\n polinomio_2_poly1d.root = {polinomio_2_poly1d.roots}'
      f'\n polinomio_3_poly1d.root = {polinomio_3_poly1d.roots}')


x = np.linspace(-3.5, 3.5, 100)
y = 1*x**3 - 2*x**2 - 5*x + 6
plt.plot(x, y, 'b--')
plt.axhline(color='orange', linestyle='--', label='y = 0')
plt.grid()
# plt.show()


# Operações: Adição, Subtração, Multiplicação e Divisão 
print('\n' *50)

print(f'Adição: polyadd(): '
      f'\n{np.polyadd(polinomio_3_poly1d, polinomio_3_poly1d)}')

print(f'Subtração: polysub(): '
      f'\n{np.polysub(polinomio_1_poly1d, polinomio_3_poly1d)}')

print(f'Multiplicação: polymul(): '
      f'\n{np.polymul(polinomio_1_poly1d, 2)}')

quociente, resto = np.polydiv(polinomio_1_poly1d, polinomio_1_poly1d)
print(f'Divisão: polydiv():\n'
      f'Polinômio dividido: {polinomio_1_poly1d}\n'
      f'Resultado da divisão: {np.polydiv(polinomio_1_poly1d, polinomio_1_poly1d)}\n'
      f'Quociente: {quociente}\n'
      f'Resto: {resto}')