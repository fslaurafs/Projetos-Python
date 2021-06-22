# ÍNDICE DE MASSA CORPORAL
peso = float(input("Informe o peso em Kg: "))
alt = float(input("Informe a altura em m: "))

imc = peso / alt ** 2  # para usar o pow() é preciso criar uma variável
print("O IMC é: {:.1f}".format(imc))

if imc < 18.5:
    print("Você está \033[33mABAIXO DO PESO\033[m!")
elif 18.5 <= imc < 25:
    print("\033[34mPARABÉNS\033[m! Você está na faixa de \033[34mPESO IDEAL\033[m!")
elif 25 <= imc < 30:
    print("Você está em \033[33mSOBREPESO\033[m!")
elif 30 <= imc < 40:
    print("Você está em \033[35mOBESIDADE\033[m!")
else:
    print("Você está em \033[31mOBESIDADE MÓRBIDA\033[m, cuidado!")
