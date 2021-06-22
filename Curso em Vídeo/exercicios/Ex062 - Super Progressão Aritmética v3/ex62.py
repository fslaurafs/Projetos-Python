# SUPER PROGRESSÇÃO ARITMÉTICA V3
print('=' * 38)
print('{:^45}'.format(" \033[34m10 PRIMEIROS TERMOS DE UMA PA\033[m "))
print('=' * 38)

pt = int(input("Primeiro termo: "))
rz = int(input("Razão da PA: "))
tm = pt  # termo
ct = 1  # contador
tot = 0
mais = 10

while mais != 0:
    tot += mais
    while ct <= tot:
        print("{} -> ".format(tm), end='')
        tm += rz
        ct += 1

    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))

print("Progressão finalizada com {} termos mostrados".format(tot))
