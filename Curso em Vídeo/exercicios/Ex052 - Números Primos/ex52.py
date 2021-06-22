# NÚMEROS PRIMOS
n = int(input("Digite um número: "))
tot = 0

for s in range(1, n + 1):
    if n % s == 0:
        print("\033[32m", end='')
        tot += 1
    else:
        print("\033[31m", end='')
    print("{} ".format(s), end='')

print("\n\033[mO número {} foi divisível {} vezes".format(n, tot))

if tot == 2:
    print("E por isso ele \033[32mÉ PRIMO\033[m!")
else:
    print("E por isso ele \033[31mNÃO É PRIMO\033[m!")
