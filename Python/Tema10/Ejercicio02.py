from tkinter import *

window = Tk()

lista = ['Windows', 'macOS', 'Linux', 'MS DOS', 'AmigaOS', 'BeOS', 'OS/2']
lista_items = StringVar(value=lista)
listbox = Listbox(window, listvariable=lista_items)
listbox.grid(column=0, row=0, sticky=W)

lbl= Label(window,text='Lista de sistemas operativos')
lbl.grid(column=0, row=1, sticky=W)

window.mainloop()