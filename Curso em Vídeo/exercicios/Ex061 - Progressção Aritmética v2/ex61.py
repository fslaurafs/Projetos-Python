# PROGRESSÃO ARITMÉTICA V2
print('=' * 38)
print('{:^45}'.format(" \033[34m10 PRIMEIROS TERMOS DE UMA PA\033[m "))
print('=' * 38)

pt = int(input("Primeiro termo: "))
rz = int(input("Razão da PA: "))
tm = pt  # termo
ct = 1  # contador

while ct <= 10:
    print("{} -> ".format(tm), end='')
    tm += rz
    ct += 1

print("FIM")
