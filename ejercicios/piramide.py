""" altura = 30

for fila in range(altura + 1):
    for columna in range(1, fila + 1):
        print(columna, end="")
    print()
 """

n = 6
# int(input("introduzca un numero: "))

for i in range(n, 0, -1):
    print("")
    for j in range(1, i + 1):
        print(j, end=" ")
