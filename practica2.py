lista = [3,6,8,2,6]

def mayor(lista):
    max = lista[0];
    for x in lista:
        if x > max:
            max = x
    return max    
 
def menor(lista):
    min = lista[0];
    for x in lista:
        if x < min:
            min = x
    return min
 
def main(lista):
    print ("La lista es ", lista)
    print ("El número mayor es ", mayor(lista))
    print ("El número menor es ", menor(lista))
    print ("Usando las funciones estándar de Python")
    print ("El número mayor es: ", max(lista))
    print ("El número menos es: ", min(lista))
 
main(lista)