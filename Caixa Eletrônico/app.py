# SIMULADOR DE CAIXA ELETRÔNICO

print("\033[1;35m=\033[m" * 32)
print("{:^40}".format("\033[1;35mBANCO DEVS\033[m"))
print("\033[1;35m=\033[m" * 32)

valor = int(input("Quanto você deseja sacar? R$"))
total = valor
ced = 100
totalCed = 0

while True:
    if total >= ced:
        total -= ced
        totalCed += 1
    else:
        if totalCed > 0:
            print(f"Total de {totalCed} cédulas de R${ced}")
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totalCed = 0
        if total == 0:
            break

print("\033[1;35m=\033[m" * 45)
print("\033[1;35mVolte sempre ao BANCO DEVS! Tenha um bom dia\033[m")
print("\033[1;35m=\033[m" * 45)
