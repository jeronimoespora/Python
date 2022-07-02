numero = int(input("Ingrese un numero por favor: "))

for i in range(0, numero):

    if numero % i == 0:
        print(i, "es divisible por ", numero)
        i = i + 1
    else:
        print("Este numero no tiene divisibles!")
