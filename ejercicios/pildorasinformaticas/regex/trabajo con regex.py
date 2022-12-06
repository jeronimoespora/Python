import re

cadena = " Estoy trabajando con Python en lunes y cerca de navidad. El proximo lunes no voy a trabajar!"

busqueda = "lunes"

texto_encontrado = re.search(busqueda, cadena)

print(texto_encontrado)

print(texto_encontrado.start())

print(texto_encontrado.end())

print(texto_encontrado.span())

print(len(re.findall(busqueda, cadena)))

print(re.findall(busqueda, cadena))
