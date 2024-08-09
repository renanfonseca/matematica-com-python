# Fatoração Polinômial

# Exemplos
#   1. x**2 + 3*x
#   2. x**2 - 9
#   3. x**2 - 4*x + 4
#   4. x**2 + x - 6
#   5. x**3 - 3*x**2 - 10*x + 24

from sympy.abc import x
from sympy import factor

print(f'\nFatoração de x**2 + 3*x:'
      f'\n  factor(x**2 + 3*x) = {factor(x**2 + 3*x)}')

print(f'\nFatoração de x**2 - 9:'
      f'\n  factor(x**2 - 9) = {factor(x**2 - 9)}')


print(f'\nFatoração de x**3 - 3x**2 - 10x + 24:'
      f'\n  factor(x**3 - 3x**2 - 10x + 24) = {factor( x**3 - 3*x**2 - 10*x + 24 )}')