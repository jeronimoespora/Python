renta = float(input("Por favor introduce el numero de renta: "))

if renta < 12000:
    print("A la renta de", renta, "le corresponde un 7 % de tipo impositivo")
elif renta >= 12000 and renta <= 18000:
    print("A la renta de", renta, "le corresponde un 15 % de tipo impositivo")
elif renta >= 18000 and renta <= 35000:
    print("A la renta de", renta, "le corresponde un 21 % de tipo impositivo")
elif renta >= 35000 and renta <= 70000:
    print("A la renta de", renta, "le corresponde un 35 % de tipo impositivo")
else:
    print("A la renta de", renta, "le corresponde un 45 % de tipo impositivo")
