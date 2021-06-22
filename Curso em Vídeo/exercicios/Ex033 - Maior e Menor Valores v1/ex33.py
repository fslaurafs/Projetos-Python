# MAIOR E MENOR VALORES
a = int(input("Informe o primeiro número inteiro: "))
b = int(input("Informe o segundo número inteiro: "))
c = int(input("Informe o terceiro número inteiro: "))

# Verificando o MENOR:
menor = a
if b < a and b < c:
    mennor = b
if c < a and c < b:
    menor = c
print("O MENOR valor é {}.".format(menor))

# Verificando o MAIOR:
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O MAIOR valor é {}.".format(maior))
