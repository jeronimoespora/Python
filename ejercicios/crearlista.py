""" Crear una lista con los cuadrados de los números entre 1 y N (ambos 
incluidos), donde N se ingresa desde el teclado. Luego se solicita imprimir los 
últimos 10 valores de la lista.
"""


n = int(input("Ingresa un numero: "))

lista = [0]

for i in range(1, n + 1):

    i = i**2

    lista.append(i)

contador=0
for i in reversed(lista):
    contador+=1
    if contador==11:
        break
    else:
        print(i)
