# PROGRESSÃO ARITMÉTICA
print('=' * 38)
print('{:^45}'.format(" \033[34m10 PRIMEIROS TERMOS DE UMA PA\033[m "))
print('=' * 38)

pt = int(input("Primeiro termo: "))
rz = int(input("Razão: "))
dt = pt + (10 - 1) * rz  # fórmula do décimo termo de uma PA

for c in range(pt, dt + rz, rz):
    print('{} '.format(c), end='-> ')

print("FIM!")
