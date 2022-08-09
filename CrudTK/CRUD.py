# importar bibliotecas

from email import message
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

# Desarrpññp de ña omterfaz grafoca

root = Tk()
root.title("Aplicación CRUD con Base de Datos")
root.geometry("600x350")

miId = StringVar()
miNombre = StringVar()
miCargo = StringVar()
miSalario = StringVar()


def conexionBBDD():
    miConexion = sqlite3.connect("base")
    miCursor = miConexion.cursor()

    try:
        miCursor.execute(
            """
            CREATE TABLE empleado ( 
            ID INTEGER PRIMARY KEY AUTOINCREMENT
            NOMBRE VARCHAR(50) NOT NULL,
            CARGO VARCHAR(50) NOT NULL,
            SALARIO INT NOT NULL)
        
            """
        )

        messagebox.showinfo("CONEXION", "Tabla Creada exitosamente")
    except:
        messagebox.showinfo("CONEXION", "Conexion exitosa con la base de datos")


def eliminarBBDD():
    miConexion = sqlite3.connect("base")
    miCursor = miConexion.cursor()
    if messagebox.askylesno(
        message="¿Los Datos se perderan definitivamente. Desea continuar?",
        title="ADVERTENCIA",
    ):
        miCursor.execute("DROP TABLE empleado")
    else:
        pass


def salirAplicacion():
    valor = messagebox.askquestion(
        "Salir", "Esta seguro de que desea salir de la aplicacion?"
    )
    if valor == "yes":
        root.destroy()


def limpiarCampos():
    miId.set("")
    miNombre.set("")
    miCargo.set("")
    miSalario.set("")


def mensaje():
    acerca = """
    Aplicacion CRUD
    Version 1.0
    Tecnologia Python Tkinter
    """


####################################### Metodos CRUD#################################


def crear():
    miConexion = sqlite3.connect("base")
    miCursor = miConexion.cursor()
    try:
        datos = miNombre.get(), miCargo.get(), miSalario.get()
        miCursor.execute("INSERT INTO empleado VALUES(NULL,?,?,?)", (datos))
        miConexion.commit()
    except:
        messagebox.showwarning(
            "ADVERTENCIA",
            "Ocurrio un error al crear el registro, verifique conexion con BBDD",
        )
        pass
    limpiarCampos()
    mostrar()


def mostrar():
    miConexion = sqlite3.connect("base")
    miCursor = miConexion.cursor()
    registros = tree.get_children()
    for elemento in registros:
        tree.delete(elemento)

    try:
        miCursor.execute("SELECT * FROM empleado")
        for row in miCursor:
            tree.insert("", 0, text=row[0], values=(row[1], row[2], row[3]))
    except:
        pass


def actualizar():
    miConexion = sqlite3.connect("base")
    miCursor = miConexion.cursor()
    try:
        datos = miNombre.get(), miCargo.get(), miSalario.get()
        miCursor.execute(
            "UPDATE empleado SET NOMBRE=?, CARGO=?, SALARIO=? WHERE ID=" + miID.get(),
            (datos),
        )
        miConexion.commit()
    except:
        messagebox.showwarning(
            "ADVERTENCIA", "Ocurrio un error al actualizar el registro"
        )
        pass
    limpiarCampos()
    mostrar()


def borrar():
    miConexion = sqlite3.connect("base")
    miCursor = miConexion.cursor()
    try:
        if messagebox.askyesno(
            message=" Realmente desea eliminar el registro?", title="ADVERTENCIA"
        ):
            miCursor.execute("DELETE FROM empleado WHERE ID=" + miId.get())
    except:
        messagebox.showwarning(
            "ADVERTENCIA", "Ocurrio un error al tratar de eliminar los registros"
        )
        pass
    limpiarCampos()
    mostrar()


tree = ttk.Treeview(height=10, columns=("#0", "#1", "#2"))
tree.place(x=0, y=130)
tree.column("#0", width=100)
tree.heading("#0", text="ID", anchor=CENTER)
tree.heading("#1", text="Nomre de empleado", anchor=CENTER)
tree.heading("#2", text="Cargo", anchor=CENTER)
tree.column("#3", width=100)
tree.heading("#3", text="Salario", anchor=CENTER)


########## Colocar widgets en la VISTA

root.mainloop()
