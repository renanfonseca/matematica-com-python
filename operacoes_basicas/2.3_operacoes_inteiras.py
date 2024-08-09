# OPERAÇÕES INTEIRAS

from math import floor, ceil

a: float = 38.88
b: float = 12.08
c: float = -23.12
d: float = 5.5


# floor(x) retorna o maior inteiro não maior que x
 
print(f'floor({a}) = {floor(a)}')
print(f'floor({b}) = {floor(b)}')
print(f'floor({c}) = {floor(c)}')
print(f'floor({d}) = {floor(d)}')


# ceil(x) retorna o menor inteiro não menor que x
print('\n')

print(f'ceil({a}) = {ceil(a)}')
print(f'ceil({b}) = {ceil(b)}')
print(f'ceil({c}) = {ceil(c)}')
print(f'ceil({d}) = {ceil(d)}')


# round(x) arredonda x para o inteiro mais próximo
print('\n')

print(f'round({a}) = {round(a)}')
print(f'round({b}) = {round(b)}')
print(f'round({c}) = {round(c)}')
print(f'round({d}) = {round(d)}')