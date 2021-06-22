# ALUGUEL DE CARROS
d = int(input('Quantos dias foram alugados? '))
k = float(input('Quantos Km foram rodados? '))
t = (d * 60) + (k * 0.15)
print('O total a pagar será de R${:.2f}.'.format(t))
