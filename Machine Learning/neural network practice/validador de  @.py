from ipaddress import summarize_address_range


mailUsuario = input("Introduce direccion de email: ")

arroba = mailUsuario.count("@")

if (
    arroba != 1
    or mailUsuario.rfind("@") == (len(mailUsuario) - 1)
    or mailUsuario.find("@") == 0
):
    print("Mail incorrecto")

else:
    print("Mail correcto")
