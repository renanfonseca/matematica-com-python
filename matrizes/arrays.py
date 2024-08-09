# A documentação de numpy não recomenda mais usar matrix(). Em vez disso é para
# usar array(), ndarray()

# Array Unidimensional em Python
# Um array unidimensional é simplesmente uma lista que pode ter elementos de
# diferentes tipos de dados

print("Array Unidimensional:")
array_1d = [1, 2, 3, 4, 5, 'teste']
print(array_1d)
print('\n')

# Array Bidimensional em Python
# um array bidimensional é representado como uma lista de listas, onde cada 
# sublista pode conter elementos de diferentes tipos de dados

array_2d = [
    [1, 2, 3],
    [4, 5, 'texto'],
    [7, 8, 9.1]
]
print("Array Bidimensional:")
for row in array_2d:
    print(row)
print('\n')

# Array em python
# https://docs.python.org/3/library/array.html
#
# a função array do módulo array é usado para criar uma lista homogenea de 
# elementos, onde todos os elementos são do mesmo tipo, especificando pelo
# typecode

import array

array_python = array.array('b', [3, 2, 5])

print("Array Bidimensional Homogeneo:")
print(array_python)
print('\n')

# Array com NumPy
#
# ndarray é o principal objeto no NumPy para manipulação de arrays 
# multidimensionais.
#
# Todos os ndarrays são homogêneos: cada item ocupa o mesmo tamanho de bloco de 
# memória, e todos os blocos são interpretados exatamente da mesma maneira. 

import numpy as np

array_numpy_2d = np.array([[1, 3], [4, 9]], np.int32)
print(f"Array Bidimensional com NumPy ({type(array_numpy_2d)}):")
print(array_numpy_2d)
print(f"Transposta:")
print(array_numpy_2d.transpose())
print('\n')

