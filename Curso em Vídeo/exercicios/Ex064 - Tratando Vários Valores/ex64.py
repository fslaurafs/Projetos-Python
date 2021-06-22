# TRATANDO VÁRIOS VALORES
n = c = s = 0
n = int(input("Informe um valor [999 para parar]: "))

while n != 999:  # o '999' é o 'flag' nesse caso
    s += n
    c += 1
    n = int(input("Informe um valor [999 para parar]: "))

print("Você digitou {} números e a soma deles é igual a {}".format(c, s))
