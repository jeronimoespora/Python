from tkinter import *

raiz = Tk()

raiz.title("Primera ventana Python")

raiz.resizable(1, 1)

raiz.iconbitmap("\favicon.ico")

raiz.geometry("700x400")  # cambia el tamaño de la ventana

raiz.config(bg="green")  # cambio el color del fondo a verde

miFrame = Frame()

miFrame.pack()

miFrame.config(bg="red")

miFrame.config(width="650", heigth="350")

raiz.mainloop()
