# CALCULADORA DE FATORIAL

n = int(input("Informe um número para calcular seu fatorial: "))
c = n
f = 1
print("Calculando \033[1;34m{}!\033[m = ".format(n), end='')

while c > 0:
    print("{}".format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1

print("\033[1;34m{}\033[m".format(f))


"""
# outra maneira:
from math import factorial
n = int(input("Informe um número para calcular seu fatorial: "))
f = factorial(n)
print("O fatorial de {} é {}".format(n, f))
"""
