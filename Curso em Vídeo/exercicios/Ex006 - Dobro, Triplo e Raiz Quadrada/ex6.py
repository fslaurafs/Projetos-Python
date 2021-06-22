# DOBRO, TRIPLO E RAIZ QUADRADA
n = int(input('Informe um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} é {}! \nO triplo de {} é {}! \nA raiz quadrada de {} é {:.2f}!'.format(n, d, n, t, n, r))

'''As variáveis podem ser colocadas direto no print (exemplo no exercício 5)
Para a raiz quadrada pode-se usar: pow(n, (1/2))'''
