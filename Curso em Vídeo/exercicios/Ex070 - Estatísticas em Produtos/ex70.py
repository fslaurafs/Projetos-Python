# ESTATÍSTICAS EM PRODUTOS
print('=' * 32)
print('{:^40}'.format(" \033[1;34mLOJAS BARATO\033[m "))
print('=' * 32)
produto = total = maiormil = menor = 0
barato = ''

while True:
    print(f"---------- {produto + 1}º PRODUTO ----------")
    nome = str(input("Nome do produto: ")).strip()
    valor = float(input("Preço: R$"))

    total += valor
    produto += 1  # contador

    if valor > 1000:
        maiormil += 1
    if produto == 1 or valor < menor:
        menor = valor
        barato = nome

    resp = ' '
    while resp not in 'SN':
        resp = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
    if resp == 'N':
        break

print("\033[1;31m{:-^32}\033[m".format(" FIM DO PROGRAMA "))
print(f">>> Total da compra: R${total:.2f}")
print(f">>> Temos {maiormil} produtos custando mais de R$1000.00")
print(f">>> O produto mais barato foi {barato} que custa R${menor:.2f}")
