# LAÇOS DE REPETIÇÃO 'FOR'
for c in range(0, 4):  # a repetição começa no 0 e para no 4
    print("Oi")
print("FIM")

for c in range(1, 6):  # a repetição começa no 1 e para no 5
    print(c)
print("FIM")

for c in range(6, 0, -1):  # a repetição é decrescente
    print(c)
print("FIM")

for c in range(0, 7, 2):  # a repetição começa no 0, para no 6 e vai de 2 em 2
    print(c)
print("FIM")

i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
for c in range(i, f + 1, p):
    print(c)
print("FIM")

s = 0
for c in range(0, 4):
    n = int(input("Digite um valor: "))
    s = s + n  # ou s += n
print("A soma dos valores é {}".format(s))
