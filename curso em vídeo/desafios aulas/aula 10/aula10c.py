# CONDIÇÕES
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))

m = (n1 + n2) / 2
print("Sua média é {:.1f}.".format(m))

if m >= 6.0:
    print("Sua média de {:.1f} é boa!".format(m))
else:
    print("Sua média de {:.1f} é ruim! Estude mais.".format(m))

# ou: print("Parabéns!" if m >= 6 else "Estude mais!")
