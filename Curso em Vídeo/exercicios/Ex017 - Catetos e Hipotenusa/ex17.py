# CATETOS E HIPOTENUSA
from math import hypot

co = float(input('Informe o cateto oposto do triângulo retângulo: '))
ca = float(input('Informe o cateto adjacente do triângulo retângulo: '))
hi = hypot(co, ca)

print('A \033[35mhipotenusa\033[m do triângulo retângulo é {:.2f}'.format(hi))

''' Sem importar módulos:
co = float(input('Informe o cateto oposto do triângulo retângulo: '))
ca = float(input('Informe o cateto adjacente do triângulo retângulo: '))
h = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa do triângulo retângulo é {:.2f}'.format(h))'''
