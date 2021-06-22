# CLASSIFICANDO ATLETAS
from datetime import date

atual = date.today().year
nasc = int(input("Informe o ano de nascimento do atleta: "))
idade = atual - nasc
print("O atleta tem {} anos.".format(idade))

if idade <= 9:
    print("Categoria: \033[34mMIRIM\033[m.")
elif idade <= 14:
    print("Categoria: \033[35mINFANTIL\033[m.")
elif idade <= 19:
    print("Categoria: \033[33mJUNIOR\033[m.")
elif idade <= 25:
    print("Categoria: \033[32mSÊNIOR\033[m.")
else:
    print("Categoria: \033[31mMASTER\033[m.")
