import sqlite3
from tkinter import END, Text, messagebox
from tkinter import simpledialog
from funcionesCRUD import *

def conectarBBDD():

    nombre_BBDD = simpledialog.askstring(
        "BBDD", "Introduce el nombre de la BBDD que quieres crear"
    )

    almacena(nombre_BBDD)

    miConexion = sqlite3.connect(nombre_BBDD)

    miCursor = miConexion.cursor()

    try:

        miCursor.execute(
            """
        
            CREATE TABLE DATOSUSUARIOS(

                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(50),
                PASSWORD VARCHAR(50),
                APELLIDO VARCHAR(50),
                DIRECCION VARCHAR(70),
                COMENTARIOS VARCHAR(120)
            )
        """
        )

        messagebox.showinfo("BBDD", "BBDD creada con éxito")

    except:
        messagebox.showwarning("¡Cuidado!", "La BBDD ya existe")


def salir_aplicacion(raiz):

    valor_salir = messagebox.askquestion(
        "Salir", "¿Seguro que deseas salir de la alplicación?"
    )
    if valor_salir == "yes":
        raiz.destroy()


def limpiar_campos(*args):

    for campo in args:

        if type(campo) == Text:

            campo.delete(1.0, END)

        else:
            campo.set("")
