# AUMENTO DE SALÁRIO
s = float(input('Informe o salário do funcionário: R$'))
t = s + (s * 15 / 100)
print('O salario de R${:.2f}, com aumento de {}15%{}, passa a ser R${:.2f}!'.format(s, '\033[32m', '\033[m', t))
