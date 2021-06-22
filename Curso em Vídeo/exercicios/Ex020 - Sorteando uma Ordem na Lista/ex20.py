# SORTEANDO UMA ORDEM NA LISTA
from random import shuffle

a1 = str(input('Informe o nome do aluno: '))
a2 = str(input('Informe o nome do aluno: '))
a3 = str(input('Informe o nome do aluno: '))
a4 = str(input('Informe o nome do aluno: '))

l = [a1, a2, a3, a4]
shuffle(l)

print('A ordem de apresentação é: ', l)
