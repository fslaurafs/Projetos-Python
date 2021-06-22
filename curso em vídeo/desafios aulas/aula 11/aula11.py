# CORES NO TERMINAL
''' \033[style; text; back m
    style       text    back    colors
0 (none)         30      40     white
1 (bold)         31      41     red
4 (underline)    32      42     green
7 (negative)     33      43     yellow
                 34      44     blue
                 35      45     magenta
                 36      46     ciano
                 37      47     gray
'''

print("\033[1;31;40m Olá mundo! \033[m")
print("\033[7;30;35m Hello world! \033[m")
print("\033[4;34mOlá mundo!\033[m")
print("\033[1;33;41m Hello world! \033[m")
print("\033[36mOlá mundo\033[m")

a = 3
b = 5
print("Os valores são \033[1;31m{}\033[m e \033[1;32m{}\033[m!".format(a, b))

nome = 'Laura'
cores = {'limpa':'\033[m',
         'azul':'\033[31m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print("Olá! Muito prazer em te conhecer, {}{}{}!".format(cores['pretoebranco'], nome, cores['limpa']))
