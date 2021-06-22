# JOGO DA ADIVINHAÇÃO
from random import randint
from time import sleep

print("-=-" * 24)
print("Vou pensar em um número entre 0 a 5. Tente descobrir qual é o número...")
print("-=-" * 24)

n = randint(0, 5)  # número escolhido pelo computador
r = int(input("Em que número estou pensando? "))  # número escolhido pelo jogador
print("\033[32mPROCESSANDO...\033[m")
sleep(2)

if r == n:
    print("\033[34mPARABÉNS! Você conseguiu me vencer!\033[m")
else:
    print("\033[31mGANHEI! Eu pensei no número {} e não no {}!\033[m".format(n, r))
