from tkinter import *
from tkinter import messagebox
from conexiones import *
from funcionesCRUD import *


class CrudPOO(Frame):
    def __init__(self, raiz):

        # ----------------Variables de control--------------------------

        self.mi_Id = StringVar()
        self.mi_nombre = StringVar()
        self.mi_apellido = StringVar()
        self.mi_password = StringVar()
        self.mi_direccion = StringVar()

        # ---------------------Barra de Menu-------------------------

        self.barraMenu = Menu(root)
        raiz.config(menu=self.barraMenu)

        super().__init__(raiz, width=300, height=300)
        self.master = raiz
        self.pack()

        self.miFrameBotones = Frame(raiz)
        self.miFrameBotones.pack()

        self.crear_widgets()

        self.crear_barra_menu()

        self.ubicar_botones()

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

    def crear_barra_menu(self):

        # --------------------MENU-------------------------------
        self.bbddMenu = Menu(self.barraMenu, tearoff=0)
        self.bbddMenu.add_command(label="Conectar", command=conectarBBDD)
        self.bbddMenu.add_command(label="Salir", command=lambda: salir_aplicacion(root))

        self.borrarMenu = Menu(self.barraMenu, tearoff=0)
        self.borrarMenu.add_command(
            label="Limpiar campos",
            command=lambda: limpiar_campos(
                self.textComentario,
                self.mi_Id,
                self.mi_nombre,
                self.mi_password,
                self.mi_apellido,
                self.mi_direccion,
            ),
        )

        self.crudMenu = Menu(self.barraMenu, tearoff=0)
        self.crudMenu.add_command(
            label="Crear",
            command=lambda: crear(
                self.mi_nombre,
                self.mi_password,
                self.mi_apellido,
                self.mi_direccion,
                self.textComentario.get(1.0, END),
            ),
        )
        self.crudMenu.add_command(
            label="leer",
            command=lambda: leer(
                self.mi_Id.get(),
                self.mi_nombre,
                self.mi_password,
                self.mi_apellido,
                self.mi_direccion,
                self.textComentario,
            ),
        )

        self.crudMenu.add_command(label="Actualizar")
        self.crudMenu.add_command(label="Borrar")

        self.ayudaMenu = Menu(self.barraMenu, tearoff=0)
        self.ayudaMenu.add_command(label="Licencia")
        self.ayudaMenu.add_command(label="Acerca de...")

        self.barraMenu.add_cascade(label="BBDD", menu=self.bbddMenu)
        self.barraMenu.add_cascade(label="Borrar", menu=self.borrarMenu)
        self.barraMenu.add_cascade(label="CRUD", menu=self.crudMenu)
        self.barraMenu.add_cascade(label="Ayuda", menu=self.ayudaMenu)

    def ubicar_botones(self):
        self.botonCrear = Button(self.miFrameBotones, text="Crear")
        self.botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

        self.botonLeer = Button(self.miFrameBotones, text="Leer")
        self.botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

        self.botonActualizar = Button(self.miFrameBotones, text="Actualizar")
        self.botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

        self.botonBorrar = Button(self.miFrameBotones, text="Borrar")
        self.botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)


root = Tk()

app = CrudPOO(root)
app.mainloop()
