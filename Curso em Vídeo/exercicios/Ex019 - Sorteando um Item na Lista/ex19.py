# SORTEANDO UM ITEM NA LISTA
from random import choice

a1 = str(input('Informe o nome do primeiro aluno: '))
a2 = str(input('Informe o nome do segundo aluno: '))
a3 = str(input('Informe o nome do terceiro aluno: '))
a4 = str(input('Informe o nome do quarto aluno: '))

l = [a1, a2, a3, a4]
e = choice(l)

print('O aluno que irá apagar o quadro é: {}{}{}.'.format('\033[36m', e, '\033[m'))
