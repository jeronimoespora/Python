cadena=input("Ingresa tu frase: ")

cadena = cadena.lower()

#remplazamos estos caracteres
cadena = cadena.replace(",","")
cadena = cadena.replace(".","")

#seoaramos la cadena 
cadena = cadena.split(" ")

nuevo = []
#recorremos la cadena 
for p in cadena:
    if p not in nuevo:
        nuevo.append(p)

print(" ".join(nuevo))