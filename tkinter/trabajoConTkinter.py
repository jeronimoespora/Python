from tkinter import *

raiz=Tk()

raiz.title("Primera ventana Python")

raiz.resizable(1,1)

#raiz.geometry("700x400")

raiz.config(bg="green")

miFrame=Frame()

miFrame.pack()

miFrame.config(bg="red")

miFrame.config(width="650",height="350")



raiz.mainloop()