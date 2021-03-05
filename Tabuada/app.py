# CALCULADORA DE TABUADA

c = 0

while True:
    n = int(input('Informe um número para ver sua tabuada [-1 para parar]: '))
    print('-' * 45)

    if n < 0:
        break

    print(f"\033[1;35mA tabuada de {n} é:\033[m")

    for c in range(0, 11):
        print(f"{n} x {c:2} = {n*c}")

    print('-' * 45)

print("\033[1;31mPROGRAMA TABUADA ENCERRADO!\033[m")
