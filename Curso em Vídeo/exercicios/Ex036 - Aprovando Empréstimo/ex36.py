# APROVANDO EMPRÉSTIMO
cas = float(input("Qual é o valor da casa? R$"))
sal = float(input("Salário do comprador: R$"))
pag = int(input("Quantos ANOS de financiamento? "))

pres = cas / (pag * 12)
por = sal * 30 / 100

if pres > por:
    print("\033[1;31mEMPRÉSTIMO NEGADO!\033[m")
else:
    print("\033[1;34mEMPRÉSTIMO ACEITO!\033[m")
print("Para pagar uma casa de R${:.2f} em {} anos a prestação será de {:.2f}!".format(cas, pag, pres))
