# TIPOS DE TRIÂNGULO

print("-=" * 12)
print("{}Analisador de Triângulos{}".format('\033[1;36m', '\033[m'))
print("-=" * 12)

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

# regra para formar um triângulo
a = r2 - r3 < r1 < r2 + r3
b = r1 - r3 < r2 < r1 + r3
c = r1 - r2 < r3 < r1 + r2

if a and b and c == True:
    print("Os segmentos acima {}PODEM{} formar um triângulo".format('\033[33m', '\033[m'), end=' ')
    if r1 == r2 == r3:
        print("{}EQUILÁTERO{}!".format('\033[32m', '\033[m'))
    elif r1 != r2 != r3 != r1:
        print("{}ESCALENO{}!".format('\033[35m', '\033[m'))
    else:
        print("{}ISÓCELES{}!".format('\033[34m', '\033[m'))
else:
    print("Os segmentos acima {}NÃO PODEM{} formar um triângulo!".format('\033[31m', '\033[m'))


'''
#  ANALISADOR DE TRIÂNGULOS BÁSICO
print("-=" * 12)
print("{}Analisador de Triângulos{}".format('\033[34m', '\033[m'))
print("-=" * 12)

r1 = float(input("Primeiro segmento: "))    # segmento 1
r2 = float(input("Segundo segmento: "))     # segmento 2
r3 = float(input("Terceiro segmento: "))    # segmento 3

# regras de triângulo verdadeiro
a = r2 - r3 < r1 < r2 + r3
b = r1 - r3 < r2 < r1 + r3
c = r1 - r2 < r3 < r1 + r2

if a and b and c == True:
    print("Os segmentos acima {}PODEM{} formar um triângulo!".format('\033[32m', '\033[m'))
else:
    print("Os segmentos acima {}NÃO PODEM{} formar um triângulo!".format('\033[31m', '\033[m'))

# outra maneira:
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM formar um triângulo!")
else:
    print("Os segmento acima NÃO PODEM formar um triângulo!")
'''
