# CRIANDO UM MENU DE OPÇÕES
from time import sleep

n1 = int(input("Informe o \033[1;32mprimeiro\033[m número: "))
n2 = int(input("Informe o \033[1;34msegundo\033[m número: "))
o = 0

while o != 5:
    sleep(1)
    print(""">>> MENU DE INTERAÇÃO:
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA""")
    o = int(input(">>> Qual opção você deseja? "))

    if o == 1:
        s = n1 + n2
        print("A SOMA: \033[1;32m{}\033[m + \033[1;34m{}\033[m é {}".format(n1, n2, s))
    elif o == 2:
        m = n1 * n2
        print("A MULTIPLICAÇÃO: \033[1;32m{}\033[m x \033[1;34m{}\033[m é {}".format(n1, n2, m))
    elif o == 3:
        if n1 > n2:
            print("Entre {} e {} o \033[1;35mMAIOR\033[m é \033[1;32m{}\033[m".format(n1, n2, n1))
        if n1 == n2:
            print("Não existe valor maior. Ambos são \033[1;33mIGUAIS\033[m")
        else:
            print("Entre {} e {} o \033[1;35mMAIOR\033[m é \033[1;34m{}\033[m".format(n1, n2, n2))
    elif o == 4:
        n1 = int(input("Informe o \033[1;32mprimeiro\033[m valor: "))
        n2 = int(input("Informe o \033[1;34msegundo\033[m valor: "))
    elif o > 5:
        print("Opção \033[1;31mINVÁLIDA!\033[m Tente novamente!")
    else:
        print("\033[1;33mFinalizando...\033[m")

    print("=-=" * 15)
    sleep(2)

print("Fim do programa! Volte sempre!")
