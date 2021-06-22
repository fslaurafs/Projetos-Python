# SOMA ÍMPARES MÚLTIPLOS DE 3
print("Números \033[1;32mÍMPARES\033[m e \033[1;32mMÚLTIPLOS de 3\033[m entre \033[1;32m1\033[m e \033[1;32m500\033[m:")
s = 0
c = 0

for n in range(1, 501, 2):
    if n % 3 == 0:
        c += 1  # ou c = c + 1
        s += n  # ou s = s + n
        print(n, end=' ')

print("\nA soma de todos os {} números é igual a \033[1;32m{}\033[m".format(c, s))
