# JOGO PAR OU ÍMPAR

from random import randint

v = 0
print("\033[1;35m=-\033[m" * 30)
print("{:^65}".format("\033[1;35mVAMOS JOGAR PAR OU ÍMPAR\033[m"))
print("\033[1;35m=-\033[m" * 30)

while True:
    jog = int(input("Informe um valor entre 0 e 10: "))
    pc = randint(0, 10)
    soma = jog + pc
    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input("Par ou ímpar [P/I]? ")).strip().upper()[0]

    print("--" * 30)
    print(f"Você jogou {jog} e o comutador jogou {pc}. Total = {soma}. ", end='')
    print("Deu PAR!" if soma % 2 == 0 else "Deu ÍMPAR!")
    print("--" * 30)

    if tipo == 'P':
        if soma % 2 == 0:
            print("\033[1;34mVOCÊ VENCEU!\033[m")
            v += 1
        else:
            print("\033[1;31mVOCÊ PERDEU!\033[m")
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print("\033[1;34mVOCÊ VENCEU!\033[m")
            v += 1
        else:
            print("\033[1;31mVOCÊ PERDEU!\033[m")
            break

    print("Vamos jogar novamente...")
    print("=-" * 30)

print("=-" * 30)
print(f"\033[1;35mGAME OVER!\033[m Você venceu {v} vezes.")
