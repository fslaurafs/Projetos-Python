# QUEBRANDO UM  NÚMERO
from math import trunc

n = float(input('Informe um número real: '))
print('O número {} tem a parte inteira {}.'.format(n, trunc(n)))

''' Sem imortar módulos:
n = float(input('Informe um número real: '))
print('O número {} tem a parte inteira {}.'.format(n, int(n)))'''
