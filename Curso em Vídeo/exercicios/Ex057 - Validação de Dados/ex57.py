# VALIDAÇÃO DE DADOS
s = str(input("Informe o sexo [M/F]: ")).strip().upper()[0]  # [0] é fatiamento caso digite completo

while s not in 'MmFf':
    s = str(input("Dados inválidos! Informe o sexo [M/F] novamnte: ")).strip().upper()[0]

print("Sexo \033[1;34m{}\033[m registrado com sucesso!".format(s))
