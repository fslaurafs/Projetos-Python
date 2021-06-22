# GERENCIADOR DE PAGAMENTOS
print('{:=^40}'.format(" \033[34mLOJAS TUDO\033[m "))
prc = float(input("Informe o preço da compra: R$"))

print("""\nFormas de Pagamento:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
pag = int(input("Em qual opção deseja efetuar o pagamento? "))

if pag == 1:
    tot = prc - (prc * 10 / 100)
elif pag == 2:
    tot = prc - (prc * 5 / 100)
elif pag == 3:
    tot = prc
    parc = tot / 2
    print("Sua compra será parcelada em 2x de R${:.2f} sem juros".format(parc))
elif pag == 4:
    tot = prc + (prc * 20 / 100)
    totparc = int(input("Em quantas parcelas deseja realizar a compra? "))
    parc = tot / totparc
    print("Sua compra será parcelada em {}x de R${:.2f} com juros".format(totparc, parc))
else:
    tot = prc
    print("Opção de pagamento \033[1;31mINVÁLIDA\033[m!")
print("Sua compra de R${} vai custar R${} no final".format(prc, tot))
