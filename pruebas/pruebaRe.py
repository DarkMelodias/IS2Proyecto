from tkinter import *
import tkinter as tk


def escribaFecha(event):
    if event.char.isdigit():
        texto = entryFecha.get()
        letras = 0
        for i in texto:
            letras +=1
        if letras == 2:
            entryFecha.insert(2,":")
        elif letras == 5:
            entryFecha.insert(5,":")
    else:
        return "break"


ventana = Tk()

Label(ventana, text ='Fecha:').grid(row = 0, column = 0, pady = 10, padx = 10)
entryFecha = tk.Entry(ventana)
entryFecha.grid(row = 0, column = 1, pady = 10, padx = 10)

Label(ventana, text ='Teléfono:').grid(row = 1, column = 0, pady = 10, padx = 10)
entryTelefono = tk.Entry(ventana)
entryTelefono.grid(row = 1, column = 1, pady = 10, padx = 10)


entryFecha.bind("<Key>", escribaFecha)
entryFecha.bind("<BackSpace>", lambda _:entryFecha.delete(tk.END))

entryTelefono.bind("<Key>", escribaTelefono)
entryTelefono.bind("<BackSpace>", lambda _:entryTelefono.delete(tk.END))

ventana.mainloop()