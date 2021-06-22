# ALISTAMENTO MILITAR
from datetime import date

atual = date.today().year
nasc = int(input("Informe o ano do nascimento: "))
idade = atual - nasc
print("Quem nasceu em {} tem \033[35m{} anos\033[m em {}.".format(nasc, idade, atual))

if idade < 18:
    saldo = 18 - idade
    alist = atual + saldo
    print("Ainda faltam {} anos para o alistamento.".format(saldo))
    print("Seu alistamento será em \033[34m{}\033[m.".format(alist))
elif idade > 18:
    saldo = idade - 18
    alist = atual - saldo
    print("Você ja deveria ter se alistado há {} anos.".format(saldo))
    print("Seu alistamento foi em \033[34m{}\033[m.".format(alist))
else:
    print("Você tem que se alistar \033[31mIMEDIATAMENTE!\033[m")
