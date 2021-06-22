# SOMA
v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
s = v1 + v2
print('A soma de \033[32m{}\033[m e \033[32m{}\033[m é igual a \033[36m{}\033[m!'.format(v1, v2, s))

'''Pode-se retirar a linha 's':
print('A soma de {} e {} é igual a {}!'.format(v1, v2, v1+v2))'''
