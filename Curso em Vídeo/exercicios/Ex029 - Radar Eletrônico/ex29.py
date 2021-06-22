# RADAR ELETRÔNICO
v = float(input("Informe a velocidade atual do carro em Km/h: "))

if v > 80:
    m = (v - 80) * 7
    print("MULTADO! Você excedeu o limite de 80Km/h.")
    print("Você deve pagar uma multa de R${:.2f}!".format(m))

print("Tenha um bom dia! Dirija com segurança!")
