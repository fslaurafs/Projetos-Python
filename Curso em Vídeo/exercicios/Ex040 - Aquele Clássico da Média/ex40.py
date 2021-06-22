# AQUELE CLÁSSICO DA MÉDIA
n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))

media = (n1 + n2) / 2
print("Quem tirou {} e {} tem uma média de {}{:.1f}{}".format(n1, n2, '\033[35m', media, '\033[m'))

if media < 5.0:
    print("O aluno está \033[1;31mREPROVADO!\033[m")
elif 5.0 <= media < 7:
    print("O aluno está de \033[1;33mRECUPERAÇÃO!\033[m")
else:
    print("O aluno está \033[1;34mAPROVADO!\033[m")
