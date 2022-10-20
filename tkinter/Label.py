from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=450)

miFrame.pack()

miLabel=Label(miFrame, text="Felicitaciones, este es un label!")
miLabel.pack()

miLabel.place(x=120, y=125)

root.mainloop()