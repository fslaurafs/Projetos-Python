# APRESENTAÇÃO
nome = input('Qual o seu nome? ')
# nome = str(input('Qual o seu nome? ')) está sendo mais específico
print('Olá {}{}{}! É um prazer te conhecer!'.format('\033[1;31m', nome, '\033[m'))

'''{:10} o nome vai ficar escrito em 10 espaços
{:>10} vai ficar à esquerda em 10 espaços
{:<10} vai ficar à direita em 10 espaços
{:^10} vai ficar centralizado em 10 espaços
{:=^10} vai ficar centralizado em 10 espaços com o nome entre sinais de igual'''
