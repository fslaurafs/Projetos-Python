# SEQUÊNCIA DE FIBONACCI
print('=' * 38)
print('{:^45}'.format(" \033[34mSEQUÊNCIA DE FIBONACCI\033[m "))
print('=' * 38)

n = int(input("Quantos termos você quer mostrar? "))
t1 = 0
t2 = 1
c = 3
print("~" * 38)
print("{} -> {}".format(t1, t2), end='')

while c <= n:
    t3 = t1 + t2
    print(" -> {}".format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1

print(" -> FIM")
print("~" * 38)
