numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))


def mayorQue(numero1, numero2, numero3):
    if numero1 > numero2 and numero1 > numero3:
        print(numero1, " Es el mayor!")
    if numero2 > numero1 and numero2 > numero3:
        print(numero2, " Es el mayor!")
    if numero3 > numero2 and numero3 > numero1:
        print(numero3, " Es el mayor!")


mayorQue(numero1, numero2, numero3)
