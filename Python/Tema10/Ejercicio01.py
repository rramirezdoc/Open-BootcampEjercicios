from tkinter import *

def mostraropcion():
    lbl.config(text="{}".format(opcion.get()))

def reiniciar():
    opcion.set(None)
    lbl.config(text='')

window = Tk()

opcion = StringVar()
opcion.set(None)
r1 = Radiobutton(window, text='Opcion 1', value='Op1', variable=opcion, command=mostraropcion).pack(anchor=W)
r2 = Radiobutton(window, text='Opcion 2', value='Op2', variable=opcion, command=mostraropcion).pack(anchor=W)
r3 = Radiobutton(window, text='Opcion 3', value='Op3', variable=opcion, command=mostraropcion).pack(anchor=W)
r4 = Radiobutton(window, text='Opcion 4', value='Op4', variable=opcion, command=mostraropcion).pack(anchor=W)

lbl = Label(window)
lbl.pack()

Button(window, text='Reset',command=reiniciar).pack()

window.mainloop()