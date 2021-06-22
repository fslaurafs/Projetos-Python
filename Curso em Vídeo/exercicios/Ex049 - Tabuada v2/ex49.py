# TABUADA V2
n = int(input('Informe um número para ver sua tabuada: '))
print('\033[31mA tabuada de {} é:\033[m'.format(n))
print('-' * 14)

for c in range(0, 11):
    print("{} x {:2} = {}".format(n, c, n*c))

print('-' * 14)
