# CALCULADORA SEQUÊNCIA DE FIBONACCI

print("\033[1;34mSequência de fibonacci\033[m")
num = int(input("Quantos termos você quer ver? "))

t1 = 0      # primeiro termo da sequência
t2 = 1      # segundo termo da sequência
count = 3   # contador

print("\033[0;34m{} -> {}\033[m".format(t1, t2), end='')

while count <= num:
    t3 = t2 + t1
    print("\033[0;34m -> {}\033[m".format(t3), end='')
    t1 = t2
    t2 = t3
    count += 1

print("\033[0;34m \033[m-> FIM")
