# CONDIÇÕES ANINHADAS
nome= str(input("Qual o seu nome? "))

if nome == 'Laura':
    print("Que nome bonito!")
elif nome == 'Maria' or nome == 'João':
    print("Seu nome é bem popular no Brasil!")
elif nome == 'Enzo' or nome == 'Valentina':
    print("Muita gente acha seu nome feio!")
elif nome in 'Isabela Bruna Mariana Gustavo':
    print("Vem de zap rsrs!")
else:
    print("Seu nome é sem graça!")

print("Tenha um bom dia, {}!".format(nome))
