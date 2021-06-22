# PREÇO COM DESCONTO
v = float(input('Informe o valor do produto: R$'))
p = v - (v * 5 / 100)
print('O preço produto de R${:.2f} com {}5%{} de desconto fica R${:.2f}'.format(v, '\033[32m', '\033[m', p))
