# CONTAGEM REGRESSIVA
from time import sleep
print("Contagem regressiva para queima de fogos de artifício:")

for c in range(10, -1, -1):
    print(c)
    sleep(1)

print("\033[4;31mBUUM! BUM! POOOW!\033[m")
