totalCompra = int(input("Ingrese el total de la compra: "))
pago = int(input("Ingrese monto del pago: "))


def calculoVuelto(pago, totalCompra):
    if totalCompra > pago:
        vuelto = "El total a pagar no puede ser mayor que el pago"
    else:
        vuelto = pago - totalCompra
    return vuelto
    
vuelto=(calculoVuelto(pago, totalCompra))
print("El vuelto es: ",vuelto)



if vuelto >= 500:
    queda = vuelto // 500
    print(str(queda)+" de 500")
    vuelto = vuelto % 500
    #print("Faltan "+ str (vuelto)+" pesos ")

if vuelto >= 100:
    queda = vuelto // 100
    print(str(queda)+" de 100")
    vuelto = vuelto % 100
    #print("Faltan "+ str (vuelto)+" pesos ")

if vuelto >= 50:
    queda = vuelto // 50
    print( str(queda)+" de 50")
    vuelto = vuelto % 50
    #print("Faltan "+ str (vuelto)+" pesos ")
    
if vuelto >= 20:
    queda = vuelto // 20
    print(str(queda)+" de 20")
    vuelto = vuelto % 20
    #print("Faltan "+ str (vuelto)+" pesos ")

if vuelto >= 10:
    queda = vuelto // 10
    print( str(queda)+" de 10")
    vuelto = vuelto % 10
    #print("Faltan "+ str (vuelto)+" pesos ")

if vuelto >= 5:
    queda = vuelto // 5
    print( str(queda)+" de 5")
    vuelto = vuelto % 5
    #print("Faltan "+ str (vuelto)+" pesos ")
    
if vuelto >= 1:
    queda = vuelto // 1
    print( str(queda)+" de 1")
    vuelto = vuelto % 1
    #print("Faltan "+ str (vuelto)+" pesos ")
    