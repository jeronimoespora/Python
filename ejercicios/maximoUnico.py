""" Desarrollar una función que reciba tres números positivos y devuelva el mayor 
de los tres, sólo si éste es único (mayor estricto). En caso de no existir el mayor 
estricto devolver -1. No utilizar operadores lógicos (and, or, not). Desarrollar 
también un programa para ingresar los tres valores, invocar a la función y 
mostrar el máximo hallado, o un mensaje informativo si éste no existe. """


def obtenerNumerosPositivos():
    

    n1 = int(input("Ingrese el primer numero: "))
    while n1 <= 0:
        n1 = int(input("Por favor, ingrese un numero positivo: "))

    n2 = int(input("Ingrese el segundo numero: "))
    while n2 <= 0:
        n2 = int(input("Por favor, ingrese un numero positivo: "))

    n3 = int(input("Ingrese el tercer numero: "))
    while n3 <= 0:
        n3 = int(input("Por favor, ingrese un numero positivo: "))
    
    resultado=[n1,n2,n3]
    return resultado


lista=obtenerNumerosPositivos()

max=max(lista)
contador=0

n1=lista[0]
n2=lista[1]
n3=lista[2]


if max == n1:
    contador+=1
if max == n2:
    contador+=1
if max == n3:
    contador+=1

if contador >1:
    print("-1 = no podemos obtener un maximo estricto!")
else:
    print(max)