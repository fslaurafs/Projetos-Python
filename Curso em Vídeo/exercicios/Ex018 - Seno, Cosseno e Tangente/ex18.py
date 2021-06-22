# SENO COSSENO E TANGENTE
from math import radians, sin, cos, tan

n = float(input('Informe um ângulo em graus: '))
s = sin(radians(n))
c = cos(radians(n))
t = tan(radians(n))

print('O SENO de {}° é {:.2f} \nO COSSENO de {}° é {:.2f} \nA TANGENTE de {}° é {:.2f}'.format(n, s, n, c, n, t))
