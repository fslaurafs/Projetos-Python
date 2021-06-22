# GRUPO DA MAIORIDADE
from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0

for pess in range(1, 8):
    nasc = int(input("Em que ano a {}ª pessoa nasceu? ".format(pess)))
    idade = atual - nasc

    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

print("\nAo todo, temos {} pessoas que já atingiram a maioridade.".format(totmaior))
print("E também temos {} pessoas que ainda não atingiram a maioridade.".format(totmenor))
