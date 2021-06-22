# DETECTOR DE PALÍNDROMO
frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):  # contagem começa em 0, contagem inclui a 1° letra, regressivo
    inverso += junto[letra]

print("O inverso de {} é {}".format(junto, inverso))

if inverso == junto:
    print("Temos um \033[1;34mPALÍNDROMO\033[m!")
else:
    print("A frase digitada \033[1;31mNÃO É\033[m um palíndromo!")

"""No lugar do *inverso =''* e do 'for' pode-se usar a técnica do fatiamento:
inverso = junto[::-1]"""
