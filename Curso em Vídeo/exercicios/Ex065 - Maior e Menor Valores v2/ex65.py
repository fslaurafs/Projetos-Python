# MAIOR E MENOR VALORES
resp = "S"
som = qnt = med = maior = menor = 0

while resp in 'Ss':
    val = int(input("Informe um valor: "))
    som += val
    qnt += 1

    if qnt == 1:
        maior = menor = val
    else:
        if val > maior:
            maior = val
        if val < menor:
            menor = val

    resp = str(input("Deseja continuar [S/N]? ")).upper().strip()[0]

med = som / qnt
print("Você digitou {} números e a média deles foi {:.2f}".format(qnt, med))
print("O maior valor digitado foi {} e o menor foi {}".format(maior, menor))
