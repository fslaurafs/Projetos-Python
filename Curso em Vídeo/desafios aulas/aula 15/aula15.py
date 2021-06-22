# INTERROMPENDO REPETIÇÕES 'WHILE'
n = s = 0
while True:
    n = int(input("Informe um valor: "))
    if n == 999:
        break
    s += n
# print("A soma vale {}".format(s))
print(f"A soma vale {s}")

'''s = 0
n = int(input("Informe um valor: "))
while n != 999:
    s += n
    n = int(input("Informe um valor: "))
print("A soma vale {}".format(s))'''

nome = 'José'
idade = 33
salario = 987.35
print(f"O {nome} tem {idade} anos e recebe R${salario}")
"""{nome:^20} centraliza em 20 espaços
{nome:-^20} centraliza entre traços em 20 espaços
{nome:>20} alinhado à direita
{nome:<20} alinhado à esquerda"""
