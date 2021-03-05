# JOGO PEDRA, PAPEL OU TESOURA

from random import randint
from time import sleep

print("\033[1;35m=-=\033[m" * 7)
print("Let's play \033[1;35mJOKENPO\033[m")
print("\033[1;35m=-=\033[m" * 7)

itens = ("PEDRA", "PAPEL", "TESOURA")
pc = randint(0, 2)  # escolha do computador

print("""Estas são suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura""")
player = int(input("Qual a sua escolha? "))  # escolha do jogador
print("\033[1;35m=-=\033[m" * 7)

print("\033[1;35mJO\033[m")
sleep(1)
print("\033[1;35mKEN\033[m")
sleep(1)
print("\033[1;35mPO\033[m")
sleep(2)

print("\033[1;35m=-=\033[m" * 8)
print("Jogador escolheu {}".format(itens[player]))
print("Computador escolheu {}".format(itens[pc]))
print("\033[1;35m=-=\033[m" * 8)

if pc == player:
    print("\033[1;33mEMPATE\033[m")

elif pc == 0 and player == 2 or pc == 1 and player == 0 or pc == 2 and player == 1:
    print("\033[1;31mCOMPUTADOR VENCEU!\033[m")

elif player == 0 and pc == 2 or player == 1 and pc == 0 or player == 2 and pc == 1:
    print("\033[1;32mJOGADOR VENCEU!\033[m")
    
else:
    print("\033[1;31mOPÇÃO INVÁLIDA!\033[m")


"""
# outra maneira:

if pc == 0:
    if player == 0:
        print("\033[1;33mEMPATE\033[m")
    elif player == 1:
        print("\033[1;32mJOGADOR VENCEU!\033[m")
    elif player == 2:
        print("\033[1;31mCOMPUTADOR VENCEU!\033[m")
    else:
        print("\033[1;31mOPÇÃO INVÁLIDA!\033[m")

elif pc == 1:
    if player == 0:
        print("\033[1;31mCOMPUTADOR VENCEU!\033[m")
    elif player == 1:
        print("\033[1;33mEMPATE!\033[m")
    elif player == 2:
        print("\033[1;32mJOGADOR VENCEU!\033[m")
    else:
        print("\033[1;31mOPÇÃO INVÁLIDA!\033[m")

elif pc == 2:
    if player == 0:
        print("\033[1;32mJOGADOR VENCEU!\033[m")
    elif player == 1:
        print("\033[1;31mCOMPUTADOR VENCEU!\033[m")
    elif player == 2:
        print("\033[1;33mEMPATE!\033[m")
    else:
        print("\033[1;31mOPÇÃO INVÁLIDA!\033[m")
"""
