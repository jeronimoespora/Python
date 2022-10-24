from tkinter import *

raiz=Tk()

miFrame=Frame(raiz, width=1000, height=550)
miFrame.pack()



#cuadroTexto=Entry(raiz)

cuadroTextoNombre=Entry(miFrame)
cuadroTextoNombre.grid(row=0, column=1)

nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0)

cuadroTextoApellido=Entry(miFrame)
cuadroTextoApellido.grid(row=1, column=1)

nombreLabel=Label(miFrame, text="Apellido: ")
nombreLabel.grid(row=1, column=0)

cuadroTextoMail=Entry(miFrame)
cuadroTextoMail.grid(row=2, column=1)

nombreLabel=Label(miFrame, text="mail: ")
nombreLabel.grid(row=2, column=0)

cuadroTextoDireccion=Entry(miFrame)
cuadroTextoDireccion.grid(row=3, column=1)

nombreLabel=Label(miFrame, text="direccion: ")
nombreLabel.grid(row=3, column=0)


raiz.mainloop()

