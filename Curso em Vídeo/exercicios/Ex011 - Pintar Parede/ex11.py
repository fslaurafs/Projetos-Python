# PINTAR PAREDE
l = float(input('Informe a largura em metros da parede: '))
h = float(input('Informe a altura em metros da parede: '))
a = l * h
t = a / 2
print('A dimensão da parede é {}x{} e possui área \033[34m{}m²\033[m.'.format(l, h, a))
print('Serão necessários \033[34m{}L\033[m de tinta para pintar a parede.'.format(t))
