# AUMENTOS MÚLTIPLOS
s = float(input("Informe o salário do funcionário: R$"))

if s > 1250.00:
    sn = s + (s * 10 /100)
    print("Quem ganhava R${:.2f} passa a ganhar R${:.2f}".format(s, sn))
else:
    sn = s + (s * 15 / 100)
    print("Quem ganhava R${:.2f} passa a ganhar R${:.2f}".format(s, sn))
