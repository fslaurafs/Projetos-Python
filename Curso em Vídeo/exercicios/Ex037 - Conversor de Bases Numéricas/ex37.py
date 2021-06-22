# CONVERSOR DE BASES NUMÉRICAS
print('\033[34m-=\033[m' * 11)
print("\033[1;36m Conversor Numérico \033[m")
print('\033[34m-=\033[m' * 11)

num = int(input("\nDigite um número inteiro: "))
print("""Escolha uma das bases para conversão:
{}[ 1 ]{} para BINÁRIO
{}[ 2 ]{} para OCTAL
{}[ 3 ]{} para HEXADECIMAL
[ 4 ] para TODAS as anteriores""".format('\033[31m', '\033[m', '\033[32m', '\033[m', '\033[34m', '\033[m'))
con = int(input("Sua opção: "))

b = bin(num)
o = oct(num)
h = hex(num)

# usar o 'fatiamento' ([2:]) para retirar a base que aparece (0b, 0o, 0x)
if con == 1:
    print("\nO número \033[31m{}\033[m convertido para BINÁRIO é igual a \033[31m{}\033[m.".format(num, b[2:]))
elif con == 2:
    print("\nO número \033[32m{}\033[m convertido para OCTAL é igual a \033[32m{}\033[m.".format(num, o[2:]))
elif con == 3:
    print("\nO número \033[34m{}\033[m convertido para HEXADECIMAL é igual a \033[34m{}\033[m.".format(num, h[2:]))
elif con == 4:
    print("\nO número \033[31m{}\033[m convertido para BINÁRIO é igual a \033[31m{}\033[m.".format(num, b[2:]))
    print("O número \033[32m{}\033[m convertido para OCTAL é igual a \033[32m{}\033[m.".format(num, o[2:]))
    print("O número \033[34m{}\033[m convertido para HEXADECIMAL é igual a \033[34m{}\033[m.".format(num, h[2:]))
else:
    print("Opção {} {}INVÁLIDA{}!".format(con, '\033[1;31m', '\033[m'))
