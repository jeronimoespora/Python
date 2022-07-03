contador = 0
for i in range(1, 500):
    print(i)
    if i % 4 == 0:
        print("Multiplo de 4")
    if i % 9 == 0:
        print("Multiplo de 9")
    contador += 1
    if contador == 5:
        print("------------------------")
        contador = 0
