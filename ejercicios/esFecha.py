



def obtenerfecha():
    
    
    n1 = int(input("Ingrese el numero del dia: "))
    while n1 <= 0:
        n1 = int(input("Por favor, ingrese un numero positivo: "))
    

    n2 = int(input("Ingrese el numero para el mes: "))
    while n2 <= 0:
        n2 = int(input("Por favor, ingrese un numero positivo: "))
    

    n3 = int(input("Ingrese el tercer numero: "))
    while n3 <= 0:
        n3 = int(input("Por favor, ingrese un numero para un año: "))
    
    
    if n1 > 31 or n2 > 12 or n3 > 2023:
        return False
    else:
        return True


print(obtenerfecha())



