# MAIOR E MENOR DA SEQUÊNCIA
maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input("Peso em Kg da {}ª pessoa: ".format(p)))

    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print("\nO \033[1;34mMAIOR\033[m peso é {}Kg".format(maior))
print("O \033[1;33mMENOR\033[m peso é {}Kg".format(menor))
