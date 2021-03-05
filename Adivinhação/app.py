# JOGO DA ADIVINHAÇÃO

from random import randint
from time import sleep

print("-=-" * 14)
print("Estou pensando em um número entre 0 e 50! \nTente adivinhar que número é...")
print("-=-" * 14)

pc = randint(0, 50)                         # número aleatório escolhido pelo computador
person = int(input("Qual é o número? "))    # número escolhido pelo jogador
attempts = 1                                # número de tentativas

print("\033[1;33mPROCESSANDO...\033[m")
sleep(2)

while person != pc:
    if person > pc:
        person = int(input("\033[1;31mMENOS\033[m... Tente de novo: "))
    elif person < pc:
        person = int(input("\033[1;31mMAIS\033[m... Tente de novo: "))

    attempts += 1
    print("\033[1;33mPROCESSANDO...\033[m")
    sleep(2)

if person == pc:
    print("\033[1;34mESSE É O NÚMERO!\033[m")
    print("Você precisou de {} tentativas".format(attempts))
