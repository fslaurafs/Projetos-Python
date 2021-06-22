# OPERADORES ARITMÉTICOS
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2  # e = pow(n1, n2)

print('A soma é {}, o produto é {} e a divisão é {}!'.format(s, m, d))
# Para a divisão, pode-se limitar as casas do número com vírgula {:.3f}
# Para não quebrar a linha: print('A soma é {}, o produto é {} e a divisão é {}!'.format(s, m, d), end=' ')
# Para quebrar a linha: print('A soma é {}, \n o produto é {} e a divisão é {}!'.format(s, m, d))
print('A divisão inteira é {} e a potencia é {}!'.format(di, e))
