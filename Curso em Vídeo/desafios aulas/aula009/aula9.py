# MANIPULANDO TEXTO
frase = 'Curso em video Python'
print(frase)
print("-" * 50)

# Fatiamento:
print("FATIAMENTO:")
print("Caracteres: ", frase[1:15:2])  # início, fim, pulo (-1 é regressivo)
print("Caracteres: ", frase[9::1])
print("-" * 50)

# Análise:
print("ANÁLISE:")
print("Tamanho: ", len(frase))  # mede o tamanho da string
print("Quantidade: ", frase.count('o'))  # quantidade do caractere desejado
print("Quantidade no período: ", frase.count('o', 0, 13))  # quantidade do caractere desejado no período (início, fim)
print("Início em: ", frase.find('deo'))  # encontra o(s) caractere(s) desejado(s) e mostra onde ele inicia
print("Início em: ", frase.find('Android'))  # quando não encontra mostra -1
print("Encontrando minúsculo: ", frase.lower().find('python'))  # primeiro deixa em minúsculo e depois encontra
print("Encontrando maiúsculo: ", frase.upper().find('VIDEO'))  # primeiro deixa em maiúsuculo e depois encontra
print("Existe? ", 'Curso' in frase)  # informa se existe ou não na string (cuidado com maiúsculas e minúsculas)
print("-" * 50)

# Transformação:
print("TRANSFORMAÇÃO:")
print("Trocar: ", frase.replace('Python', 'Android'))  # troca/reposiciona na string
print("Maiúsculo: ", frase.upper())  # troca minúsculas por maiúsculas
print("Minúsculo: ", frase.lower())  # troca por minúsculas
print("Capitalizado: ", frase.capitalize())  # capitaliza apenas a primeira
print("Capitalizando tudo: ", frase.title())  # capitaliza odas as palavras
frase1 = '   Aprenda Python  '
print(frase1)
print('Retirando o inútil: ', frase1.strip())  # retira espaços inúteis no começo e no fim da string
print("Retirando da direita: ", frase1.rstrip())  # retira espaços inúteis à direita na string
print("Retirando da esquerda: ", frase1.lstrip())  # retira espaços inúteis à esquerda na string
print("-" * 50)

# Divisão:
print("DIVISÃO:")
print("Dividindo: ", frase.split())  # divide uma string (recomeçando a contagem em cada palavra) em uma lista
dividido = frase.split()
print(dividido[2])  # mostra o item da lista split correspondente a posição desejada [x]
print(dividido[2][3])  # mostra a letra do item da lista split correspondente a posição desejada [x] e a letra [y]
print("-" * 50)

# Junção:
print("JUNÇÃO:")
print('-'.join(frase))  # troca os espaços da string por '-'
print("-" * 50)
