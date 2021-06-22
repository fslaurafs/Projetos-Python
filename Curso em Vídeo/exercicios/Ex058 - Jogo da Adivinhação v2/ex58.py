# JOGO DA ADIVINHAÇÃO V2
from random import randint
from time import sleep

print("-=-" * 24)
print("Vou pensar em um número entre 0 a 10. Tente descobrir qual é o número...")
print("-=-" * 24)

n = randint(0, 10)  # número escolhido pelo computador
r = int(input("Em que número estou pensando? "))  # número escolhido pelo jogador
t = 1  # tentativas
print("\033[32mPROCESSANDO...\033[m")
sleep(2)

while n != r:
    if r > n:
        r = int(input("Menos... Tente novamente: "))
    if r < n:
        r = int(input("Mais... Tente novamente: "))

    t += 1
    print("\033[32mPROCESSANDO...\033[m")
    sleep(2)

if r == n:
    print("\033[1;34mACERTOU!\033[m")
    print("Você precisou de {} tentativas!".format(t))
