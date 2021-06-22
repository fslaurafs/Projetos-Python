# SEPARANDO DÍGITOS DE UM NÚMERO
num = int(input("Informe um número entre 0 e 9999: "))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print("Analisando o número {}...".format(num))
print("\033[31mUnidade\033[m: {}".format(u))
print("\033[32mDezena\033[m: {}".format(d))
print("\033[33mCentena\033[m: {}".format(c))
print("\033[34mMilhar\033[m: {}".format(m))
