# UTILIZANDO MÓDULOS (BIBLIOTECAS)
import math
# Ou usar: from math import sqrt (nesse caso nao precisa por math.sqrt e math.ceil, apenas sqrt() e ceil())
n = int(input('Digite um número: '))
r = math.sqrt(n)

print('A raiz quadrada de {} é {}.'.format(n, math.ceil(r)))
# Pode-se arredondar para baixo math.floor(r) ou delimitar as casas depois da vírgula {:.2f}
