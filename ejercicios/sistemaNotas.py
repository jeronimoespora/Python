nota = int(input("Por favor ingresa la nota: "))


def calificacion(nota):
    if nota <= 3:
        print("Nota: Muy deficiente")
    elif nota == 4 or nota == 5:
        print("Nota: Insuficiente")
    elif nota == 6:
        print("Nota: Suficiente")
    elif nota == 7 or nota == 8:
        print("Nota: Bien")
    elif nota == 9:
        print("Nota: Notable")
    else:
        print("Nota: Sobresaliente")


if nota <= 10 and nota >= 1:
    print(calificacion(nota))

else:
    print("No es un numero valido!")
