from tkinter import *
from tkinter import messagebox
import sqlite3


class CrudPOO(Frame):
    def __init__(self, raiz):

        # ----------------Variables de control--------------------------

        self.mi_Id = StringVar()
        self.mi_nombre = StringVar()
        self.mi_apellido = StringVar()
        self.mi_password = StringVar()
        self.mi_direccion = StringVar()

        super().__init__(raiz, width=300, height=300)
        self.master = raiz
        self.pack()

        self.crear_widgets()

    def crear_widgets(self):

        self.cuadroId = Entry(self, textvariable=self.mi_Id)
        self.cuadroId.grid(row=0, column=1, padx=10, pady=10)

        self.cuadroNombre = Entry(self, textvariable=self.mi_nombre)
        self.cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
        self.cuadroNombre.config(fg="red", justify="right")

        self.cuadroPass = Entry(self, textvariable=self.mi_password)
        self.cuadroPass.grid(row=2, column=1, padx=10, pady=10)
        self.cuadroPass.config(show="*")

        self.cuadroApellido = Entry(self, textvariable=self.mi_apellido)
        self.cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

        self.cuadroDireccion = Entry(self, textvariable=self.mi_direccion)
        self.cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

        self.textComentario = Text(self, width=16, height=5)
        self.textComentario.grid(row=5, column=1, padx=10, pady=10)
        self.scrollVert = Scrollbar(self, command=self.textComentario.yview)
        self.scrollVert.grid(row=5, column=2, sticky="nsew")
        self.textComentario.config(yscrollcommand=self.scrollVert.set)

        # -------------------------Creación de Labels--------------------------

        self.idLabel = Label(self, text="Id:")
        self.idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

        self.nombreLabel = Label(self, text="Nombre:")
        self.nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

        self.passLabel = Label(self, text="Contraseña:")
        self.passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

        self.apellidoLabel = Label(self, text="Apellido:")
        self.apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

        self.direccionLabel = Label(self, text="Direccion:")
        self.direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

        self.comentariosLabel = Label(self, text="Comentarios:")
        self.comentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)


root = Tk()

app = CrudPOO(root)
app.mainloop()
