miDiccionario={"España":"Madrid","Francia":"Paris","Reino Unido":"Londres"}

print(miDiccionario)
def eliminarClave( diccionario, clave ):
    if clave in diccionario:
        del diccionario[ clave ]
        print(diccionario)
    return diccionario

eliminarClave(miDiccionario,miDiccionario.keys)
print(miDiccionario)