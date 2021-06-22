# PEDRA, PAPEL E TESOURA
from random import randint
from time import sleep

print("\033[35m-=\033[m" * 10)
print("Vamos jogar \033[1;35mJOKENPO!\033[m")
print("\033[35m-=\033[m" * 10)

itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
jog = int(input("Faça sua escolha: "))
print("\033[35m-=\033[m" * 10)

print("\033[1;35mJO\033[m")
sleep(1)
print("\033[1;35mKEN\033[m")
sleep(1)
print("\033[1;35mPO\033[m")
sleep(1)

print('\033[35m-=\033[m' * 12)
print("Jogador jogou {}.".format(itens[jog]))
print("Computador jogou {}.".format(itens[comp]))
print('\033[35m-=\033[m' * 12)

if comp == 0:  # PEDRA
    if jog == 0:
        print("\033[1;33mEMPATE!\033[m")
    elif jog == 1:
        print("\033[1;34mJOGADOR VENCE!\033[34m")
    elif jog == 2:
        print("\033[1;31mCOMPUTADOR VENCE!\033[m")
    else:
        print("Opção \033[1;31mINVÁLIDA\033[m!")
if comp == 1:  # PAPEL
    if jog == 0:
        print("\033[1;31mCOMPUTADOR VENCE!\033[m")
    elif jog == 1:
        print("\033[1;33mEMPATE!\033[m")
    elif jog == 2:
        print("\033[1;34mJOGADOR VENCE!\033[34m")
    else:
        print("Opção \033[1;31mINVÁLIDA\033[m!")
if comp == 2:  # TESOURA
    if jog == 0:
        print("\033[1;34mJOGADOR VENCE!\033[34m")
    elif jog == 1:
        print("\033[1;31mCOMPUTADOR VENCE!\033[m")
    elif jog == 2:
        print("\033[1;33mEMPATE!\033[m")
    else:
        print("Opção \033[1;31mINVÁLIDA\033[m!")
