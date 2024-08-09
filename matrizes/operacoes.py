# OPERAÇÕES COM MATRIZES

import numpy as np

if __name__ == "__main__":

    A_matriz2x2 = np.array([[4,9], [5, 1]])
    B_matriz2x2 = np.array([[7, 6], [1, 4]])
    print('A: ', '\n',A_matriz2x2, '\n')
    print('B: ', '\n',B_matriz2x2, '\n')

    # Adição de Matriz
    #
    # Pode ser feita com a função add(matriz_a, matriz_b) ou com operador +
    
    soma = np.add(A_matriz2x2, B_matriz2x2)
    print('A+B: ', '\n',soma, '\n')
    
    # Subtração de Matriz
    #
    #
    
    sub = np.subtract(A_matriz2x2, B_matriz2x2)
    print('A-B: ', '\n',sub, '\n')
    
    
    # Multiplicação de Matriz
    #
    #
    
    mult = np.dot(A_matriz2x2, B_matriz2x2)
    print('A*B: ', '\n',mult, '\n')
    
    mult = np.dot(B_matriz2x2, A_matriz2x2)
    print('B*A: ', '\n',mult, '\n')