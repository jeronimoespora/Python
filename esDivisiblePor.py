numero = int(input("Por favor, ingresa un numero: "))


def esDivisiblePor(numero):
    if numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0:
        if numero % 2 == 0:
            print("Es divisible por 2")
        if numero % 3 == 0:
            print("Es divisible por 3")
        if numero % 5 == 0:
            print("Es divisible por 5")
        if numero % 7 == 0:
            print("Es divisible por 7")
    else:
        print("No es divisible por uno de estos numeros")


esDivisiblePor(numero)
