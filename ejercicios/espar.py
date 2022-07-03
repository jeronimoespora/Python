par = lambda x: True if x % 2 == 0 else False
# Definimos la funcion para saber si es par

num = int(input("Ingrese el numero: "))
es_par = par(num)
# Pedimos y evaluamos el numero
print(es_par)  # aca se el resultado del lambda
if es_par:
    print("El numero es par!!")

else:
    print("El numero no es par!!")
