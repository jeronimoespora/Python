import re

lista_nombres = [
    "Antonio Banderas",
    "Salma Hayek",
    "Tomás Cruceros",
    "Antonio Resines",
    "Friedrich Hayek",
]

for nombre in lista_nombres:
    if re.findall("Hayek$", nombre):
        print(nombre)
