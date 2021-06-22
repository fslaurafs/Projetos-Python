# CONVERSOR DE TEMPERATURAS
c = float(input('Informe a tempertura em °C: '))
f = ((c * 9) /5) + 32
print('A temperatura de \033[35m{}°C\033[m corresponde a \033[35m{}°F\033[m.'.format(c, f))
