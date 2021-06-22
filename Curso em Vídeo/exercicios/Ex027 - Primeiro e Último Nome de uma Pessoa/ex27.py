# PRIMEIRO E ÚLTIMO NOME DE UMA PESSOA
nome = str(input("Informe seu nome completo: ")).strip()
n = nome.split()

print("Muito prazer em te conhecer, {}!".format(nome))
print("Seu primeiro nome é {}.".format(n[0]))
print("Seu último nome é {}.".format(n[len(n)-1]))  # tem o '-1' pois o 'split' começa e 0 e o 'len' em 1
