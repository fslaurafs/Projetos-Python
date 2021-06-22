# PRIMEIRA E ÚLTIMA OCORRÊNCIA DE UMA STRING
frase = str(input("Digite uma frase: ")).upper().strip()

print("Possui {} letras 'A' na frase.".format(frase.count('A')))
print("A primeira letra 'A' aparece na posição {}.".format(frase.find('A')+1))
print("A última letra 'A' aparece na posição {}.".format(frase.rfind('A')+1))
