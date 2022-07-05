

def esCapicua(cadena):
    esCapicua = True
    for indice in range(len(cadena)):
        if(cadena[indice] != cadena[- ( indice + 1 ) ]):
            esCapicua = False
            break
    return esCapicua

cadena = input("es capicua?  ")
esCapicuaResultado = esCapicua(cadena)

print(esCapicuaResultado)

