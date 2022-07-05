listaOrdenada = [1, 3, 5, 7, 9]
listaDesordenada = [3, 5, 4, 8, 65, 13, 25, 46, 37, 98]

print("ordenada", (listaOrdenada))
print("desordenada", listaDesordenada)

def listaordenada(lista):
    copia = ()
    copia = tuple(lista)
    
    lista.sort()

    copia = list(copia)

    if lista == copia:
        return True
    else:
        return False

print(listaordenada(listaDesordenada))
print(listaordenada(listaOrdenada))
print("ordenada", (listaOrdenada))
print("desordenada", listaDesordenada)

