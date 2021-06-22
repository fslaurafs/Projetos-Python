# VÁRIOS NÚMEROS COM 'FLAG'
s = quant = 0

while True:
    n = int(input("Informe um valor [999 para parar]: "))

    if n == 999:
        break

    quant += 1
    s += n

print(f"A soma dos {quant} números é igual a {s}!")
