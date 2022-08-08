#importar bibliotecas

from email import message
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

#Desarrpññp de ña omterfaz grafoca

root=Tk()
root.title("Aplicación CRUD con Base de Datos")
root.geometry("600x350")

miId=StringVar()
miNombre=StringVar()
MiCargo=StringVar()
miSalario=StringVar()

def conexionBBDD():
    miConexion=sqlite3.connect("base")
    miCursor=miConexion.cursor()

    try:
        miCursor.execute('''
            CREATE TABLE empleado ( 
            ID INTEGER PRIMARY KEY AUTOINCREMENT
            NOMBRE VARCHAR(50) NOT NULL,
            CARGO VARCHAR(50) NOT NULL,
            SALARIO INT NOT NULL)
        
            ''')

        messagebox.showinfo("CONEXION","Tabla Creada exitosamente")
    except:
        messagebox.showinfo("CONEXION", "Conexion exitosa con la base de datos")

def eliminarBBDD();
    miConexion=sqlite3.connect("base")
    miCursor=miConexion.cursor()
    if messagebox.askylesno(message="¿Los Datos se perderan definitivamente. Desea continuar?", title="ADVERTENCIA"):
        miCursor.execute("DROP TABLE empleado")
    else:
        pass

def salirAplicacion():
    valor=messagebox.askquestion("Salir", "Esta seguro de que desea salir de la aplicacion?"º)
    if valor ?? "yes"
        root.destroy()
