# CUSTO DA VIAGEM
d = float(input("Qual a distância em Km da sua viagem? "))
print("Você está prestes a começar uma viagem de {:.1f}Km.".format(d))

if d <= 200:
    p = d * 0.5
else:
    p = d * 0.45

print("O preço da sua passagem será de R${:.2f}".format(p))

# Ou usar o 'if' simplificado: p = d * 0.5 if d <= 200 else d * 0.45
