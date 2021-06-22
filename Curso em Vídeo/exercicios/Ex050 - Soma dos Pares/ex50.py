# SOMA DOS PARES
s = 0
c = 0

for v in range(1, 7):
    n = int(input("Informe o {}° valor inteiro: ".format(v)))

    if n % 2 == 0:
        s += n
        c += 1

print("Você informou {} números \033[1;34mPARES\033[m e a soma deles é \033[1;34m{}\033[m".format(c, s))
