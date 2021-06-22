# COMPARANDO NÚMEROS
n1 = int(input("Informe o primeiro número inteiro: "))
n2 = int(input("Informe o segundo número inteiro: "))

if n1 > n2:
    print("O {}PRIMEIRO{} valor é {}MAIOR{}.".format('\033[34m', '\033[m', '\033[34m', '\033[m'))
elif n1 < n2:
    print("O {}SEGUNDO{} valor é {}MAIOR{}.".format('\033[34m', '\033[m', '\033[34m', '\033[m'))
else:
    print("Não existe valor maior ou menor, ambos são {}IGUAIS{}.".format('\033[34m', '\033[m'))

'''Ou então:
elif n1 == n2:
    print("Não existe valor maior ou menor, ambos são {}IGUAIS{}!".format('\033[34m', '\033[m'))'''
