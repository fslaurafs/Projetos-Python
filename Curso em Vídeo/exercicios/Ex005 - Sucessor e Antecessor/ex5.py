# SUCESSOR E ANTECESSOR
n = int(input('Informe um número: '))
print('O número \033[32m{}\033[m tem antecessor \033[36m{}\033[m e sucessor \033[36m{}\033[m!'.format(n, (n-1), (n+1)))

''' Ou usar as variáveis:
a = n - 1
s = n + 1
print(''O número {} tem antecessor {} e sucessor {}!'.format(n, a, s))'''
