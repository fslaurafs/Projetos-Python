# ESTRUTURA DE REPETIÇÃO 'WHILE'
c = 1
while c < 10:
    print(c, end=' ')
    c += 1
print("\nFIM")

n = 1
while n != 0:
    n = int(input("Digite um número: "))
print("FIM")

r = 'S'
while r == 'S':
    v = int(input("Digite um valor: "))
    r = str(input("Quer continuar [S/N]? ")).upper()
print("FIM")

m = 1
par = impar = 0
while m != 0:
    m = int(input("Informe um valor: "))
    if m != 0:  # o 0 é considerado 'flag' (parada)
        if m % 2 == 0:
            par += 1
        else:
            impar += 1
print("Você digitou {} números pares e {} números ímpares.".format(par, impar))
