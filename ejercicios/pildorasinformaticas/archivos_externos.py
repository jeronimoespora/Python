import os

import io

os.makedirs("PracticaDirectorio")

os.chdir("PracticaDirectorio")

archivo_externo=open("Ejemplo.txt", "w")

archivo_externo.write("Texto de ejemplo...")


print(os.getcwd)

print(os.listdir("./"))