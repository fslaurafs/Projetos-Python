# ANALISADOR DE TEXTOS
nome = str(input("Digite seu nome completo: ")).strip()
print("Analisando seu nome...")

print("Seu nome em MAIÚSCULAS É {} ".format(nome.upper()))
print("Seu nome em MINÚSCULAS é {}".format(nome.lower()))
print("O seu nome possui {} letras ao todo.".format(len(nome) - nome.count(' ')))
separado = nome.split()
print("Seu primeiro nome é {} e ele possui {} letras.".format(separado[0], len(separado[0])))
#print("O seu primeiro nome possui {} letras.".format(nome.find(' ')))
