from tkinter import *

def select_f():
    monitor.config(text="{}".format(opcion.get()))
def reset():
    opcion.set(None)
    monitor.config(text="")

root = Tk()
opcion = StringVar()
opcion.set(None)
Radiobutton(root, text="Peugeot", variable=opcion, 
            value='Peugeot', command=select_f).pack(anchor=W)

Radiobutton(root, text="Opel", variable=opcion, 
            value='Opel', command=select_f).pack(anchor=W)
Radiobutton(root, text="Renault", variable=opcion,   
            value='Renault', command=select_f).pack(anchor=W)
Radiobutton(root, text="Seat", variable=opcion,   
            value='Seat', command=select_f).pack(anchor=W)

monitor = Label(root)
monitor.pack()
Button(root, text="Reiniciar", command=reset).pack()

root.mainloop()