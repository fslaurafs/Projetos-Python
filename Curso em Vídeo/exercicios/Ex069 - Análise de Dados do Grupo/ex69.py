# ANÁLISE DE DADOS DO GRUPO
pessoa = maioridade = quanthomem = quantmulher = 0

while True:
    print(f"---------- {pessoa + 1}º PESSOA ----------")
    idade = int(input("Informe a idade: "))
    sexo = str(input("Informe o sexo [F/M]: ")).strip().upper()[0]

    while sexo not in 'MF':
        sexo = str(input("Informe o sexo [F/M]: ")).strip().upper()[0]

    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        quanthomem += 1
    if sexo == "F" and idade < 20:
        quantmulher += 1

    cont = ' '

    while cont not in "SN":
        cont = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]

    if cont == "N":
        break

    pessoa += 1

print("\033[1;35m------- Fim do Programa ------- \033[m")
print(f">>> Total de pessoas com mais de 18 anos: {maioridade}")
print(f">>> Ao todo temos {quanthomem} homens cadastrados")
print(f">>> E temos {quantmulher} mulheres com menos de 20 anos")
