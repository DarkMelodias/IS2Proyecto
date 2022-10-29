from tkinter import *
from view_inicio import *

def run():
    root = Tk()
    root.wm_title('Manejo de Laboratorios')
    app = Interfaz(root)
    app.mainloop()

if __name__ == '__main__':
    run()