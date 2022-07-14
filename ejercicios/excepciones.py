from re import A


contador = 0
lista = []

def agregar_a_lista(lista, nombreIntroducido):
    try:
        if nombreIntroducido in lista:
            raise ValueError
        else:
            lista.append(persona)
    except ValueError:
        print("Error.Este nombre ya se ha introducido: ", nombreIntroducido)
        

while contador <10:

    persona=input("Ingresa el nombre de una persona: ")
    agregar_a_lista(lista,persona)
    contador +=1


print(lista)
