from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()

# ------------------------------Conexión/creación BBDD--------------------------------


def conectarBBDD():

    miConexion = sqlite3.connect("NegocioUsuarios")

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


def salirAplicacion():

    valor_salir = messagebox.askquestion(
        "Salir", "¿Seguro que deseas salir de la alplicación?"
    )
    if valor_salir == "yes":
        root.destroy()


def limpiar_campos():
    mi_Id.set("")
    mi_nombre.set("")
    mi_apellido.set("")
    mi_direccion.set("")
    mi_password.set("")
    textComentario.delete(1.0, END)


def crear():
    mi_conexion = sqlite3.connect("NegocioUsuarios")

    mi_cursor = mi_conexion.cursor()

    """mi_cursor.execute(
        "INSERT INTO DATOSUSUARIOS VALUES(NULL, '"
        + mi_nombre.get()
        + "','"
        + mi_password.get()
        + "','"
        + mi_apellido.get()
        + "','"
        + mi_direccion.get()
        + "','"
        + textComentario.get("1.0", END)
        + "')"
    )"""

    los_datos = (
        mi_nombre.get(),
        mi_password.get(),
        mi_apellido.get(),
        mi_direccion.get(),
        textComentario.get("1.0", END),
    )

    mi_cursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)", (los_datos))

    mi_conexion.commit()

    messagebox.showinfo("CRUD", "Registro insetado OK")


def leer():

    mi_conexion = sqlite3.connect("NegocioUsuarios")

    mi_cursor = mi_conexion.cursor()

    mi_cursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + mi_Id.get())

    datos_usuario = mi_cursor.fetchall()

    for usuario in datos_usuario:
        mi_Id.set(usuario[0])
        mi_nombre.set(usuario[1])
        mi_password.set(usuario[2])
        mi_apellido.set(usuario[3])
        mi_direccion.set(usuario[4])
        textComentario.insert(1.0, usuario[5])
    mi_conexion.commit()


def actualizar():
    mi_conexion = sqlite3.connect("NegocioUsuarios")

    mi_cursor = mi_conexion.cursor()

    """mi_cursor.execute(
        "UPDATE DATOSUSUARIOS SET NOMBRE='"
        + mi_nombre.get()
        + "', PASSWORD='"
        + mi_password.get()
        + "', APELLIDO='"
        + mi_apellido.get()
        + "', DIRECCION='"
        + mi_direccion.get()
        + "', COMENTARIOS='"
        + textComentario.get("1.0", END)
        + "' WHERE ID="
        + mi_Id.get()
    )"""

    los_datos = (
        mi_nombre.get(),
        mi_password.get(),
        mi_apellido.get(),
        mi_direccion.get(),
        textComentario.get("1.0", END),
    )

    mi_cursor.execute(
        "UPDATE DATOSUSUARIOS SET NOMBRE=?, PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIOS=? WHERE ID="
        + mi_Id.get(),
        (los_datos),
    )

    mi_conexion.commit()

    messagebox.showinfo("CRUD", "Registro actualizado OK")


def eliminar():
    mi_conexion = sqlite3.connect("NegocioUsuarios")

    mi_cursor = mi_conexion.cursor()

    mi_cursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + mi_Id.get())

    mi_conexion.commit()

    messagebox.showinfo("CRUD", "Registro borrado correctamente")


barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

# ----------------Variables de control--------------------------

mi_Id = StringVar()
mi_nombre = StringVar()
mi_apellido = StringVar()
mi_password = StringVar()
mi_direccion = StringVar()


# --------------------MENU-------------------------------
bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conectarBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Limpiar campos", command=limpiar_campos)

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=eliminar)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

# -------------------------------construccion campos grid------------------------------

miFrame = Frame(root)
miFrame.pack()

cuadroId = Entry(miFrame, textvariable=mi_Id)
cuadroId.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre = Entry(miFrame, textvariable=mi_nombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

cuadroPass = Entry(miFrame, textvariable=mi_password)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido = Entry(miFrame, textvariable=mi_apellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion = Entry(miFrame, textvariable=mi_direccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textComentario = Text(miFrame, width=16, height=5)
textComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert = Scrollbar(miFrame, command=textComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
textComentario.config(yscrollcommand=scrollVert.set)

# -------------------------Creación de Labels--------------------------

idLabel = Label(miFrame, text="Id:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passLabel = Label(miFrame, text="Contraseña:")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

apellidoLabel = Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel = Label(miFrame, text="Direccion:")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentariosLabel = Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

# ------------------------- colocación de botones-----------------

miFrameBotones = Frame(root)
miFrameBotones.pack()

botonCrear = Button(miFrameBotones, text="Crear", command=crear)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer = Button(miFrameBotones, text="Leer", command=leer)
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonActualizar = Button(miFrameBotones, text="Actualizar", command=actualizar)
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonBorrar = Button(miFrameBotones, text="Borrar", command=eliminar)
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)


root.mainloop()
