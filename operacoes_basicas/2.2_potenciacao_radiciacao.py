# 2.2 POTENCIAÇÃO E RADICIAÇÃO

import math
import numpy

# Potenciação ##################################################################
# Há 3 formás básicas de trabalhar com potenciação.
#   1. base**expoente
#   2. pow(base, expoente, modulo=null)
#   3. math.pow(base, expoente)

# Forma mais comum de potenciação
base = 5
expoente = 2
print(f'base {base} elevando ao expoente {expoente}: \n {base}**{expoente} = ' 
      f'{base**expoente}\n')
print('\n' * 30)


# pow() 
# 2 argumentos: retorno: (base ** expente)
# 3 argumentos: retorno: (base ** expoente) % modulo.
print(f'Usando função pow()')

resultado = pow(base, expoente)
print(f'pow({base}, {expoente}) = {resultado}') # Saída: 25

modulo = 3
resultado = pow(base, expoente, modulo) # Saída: 1
print(f'pow({base}, {expoente}, {modulo}) = {resultado}\n') # Saída: 25

print('\n' * 30)


# math.pow()
# math.pow() sempre retorna um float, mesmo se os argumentos forem inteiros.


base = 2
expoente = 5
resultado = math.pow(base, expoente)

print(f'Usando biblioteca math: \n math.pow({base}, {expoente}) = {resultado}')
print('\n' * 30)


# Radiciação ###################################################################
#
#   1. base**expoente_fracionario
#   2. 

# Forma direta da radiciação
base = 4
expoente_fracionario = 1/2
resultado = base**expoente_fracionario

print(f'Forma direta da radiciação:\n     {base}**{expoente_fracionario} = '
      f'{resultado}')
print('\n' * 30)


# Radiciação usando a biblioteca math, math.sqrt() para raiz quadrada
#math.sqrt() não é adequada para outras raízes.
base = 16
resultado = math.sqrt(base)
print(f'Raíz quadrada com math.sqrt():\n     math.sqrt({base}) = '
      f'{resultado}')
print('\n' * 30)


# numpy também possui funções para calcular raizes
# numpy.sqrt() para raiz quadrada
# numpy.cbrt() para raiz cúbica