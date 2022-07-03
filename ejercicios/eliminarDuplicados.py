lista=["teresa","pipo","juancho","largo"]
lista2=["juan","marcelo","teto","teresa"]
listae=[]
print(lista)
for i in lista:
    if i in lista2:
        listae.append(i)
        lista.remove(i)
    
print(listae)
print(lista)