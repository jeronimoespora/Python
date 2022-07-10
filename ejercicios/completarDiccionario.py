

paises={}

pais = input("introduce el pais: ")


while pais != "salir":
    
    ciudad=input("Introduce ciudad: ")
    lista_ciudades=paises.setdefault(pais,[ciudad])
    if lista_ciudades!=[ciudad]:
        paises[pais].append(ciudad)
    pais = input ("introduce el país: ")


print (paises)