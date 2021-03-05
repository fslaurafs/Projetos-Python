# CALCULADORA DE PROGRESSÃO ARITMÉTICA

print("\033[1;34mTERMOS DE UMA PA:\033[m")

first = int(input("Primeiro termo: "))
ratio = int(input("Razão: "))
term = first    # termo
count = 1       # countador
total = 0
more = 10       # até 10 termos

while more != 0:
    total += more  # 10 primeiros termos

    while count <= total:
        print("\033[0;34m{} -> \033[m".format(term), end='')
        term += ratio  # PA
        count += 1

    print("PAUSA")
    more = int(input("Quantos termos a mais você quer ver? (Digite 0 para parar): "))

print("Progressão encerrada com {} termos mostrados".format(total))
