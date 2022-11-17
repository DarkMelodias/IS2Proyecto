from tkinter import *
from tkinter import ttk,font
import tkinter as tk
from usuarios import *
from negocio import *
from tkinter import messagebox
from view_ingreso import *
from view_ingreso import Interfaz_inicio

class Interfaz(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        ancho_ventana = 1200
        alto_ventana = 900

        x_ventana = self.master.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.master.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.master.geometry(posicion)

        self.img_header_inicio = tk.PhotoImage(file="pic/inicio_header.png")

        self.master.resizable(0,0)
        self.create_init()
    
    def intercabio_vista(self,esconde,muestra):
        esconde.place_forget()
        if muestra == "r":
            self.create_register()
        if muestra == "i":
            self.create_init()

    def valid_ingreso(self,usr,password):
        valid = ingreso(usr,password)
        if valid == True:
            messagebox.showinfo("Ingreso","Ingreso correcto")
            self.master.withdraw()
            root = tk.Toplevel()
            root.wm_title('Manejo de Laboratorios')
            Interfaz_inicio(root,self.master)
        else:
            messagebox.showerror("Ingreso","Ingreso incorrecto,usuario o contraseña incorrectas")

    def valid_registro(self,usr,password,rpassword,r):
        if rpassword != password:
            messagebox.showerror("Registro","Registro incorrecto,contraseñas no coinciden")
        else:
            valid = registrar(usr,password)
            if valid == True:
                messagebox.showinfo("Registro","Registro correcto")
                self.intercabio_vista(r,"i")
            else:
                messagebox.showerror("Registro","Registro incorrecto,usuario ya existe")

    def create_init(self):
        self.master.configure(bg="#90B000")

        inicio = Frame(self.master)
        inicio.place(x=0, y=0, width=1200,height=900)

        header = Frame(inicio, bg="#B50900")
        header.place(x=0,y=0,height=200,width=1200)

        label = Label(header, image=self.img_header_inicio,bg="#90B000",fg="black",font=("Arial",22))
        label.place(x=0,y=0)

        body = Frame(inicio, bg="#f3e7cc")
        body.place(x=0,y=200,height=680,width=1200)

        label = Label(body, text="Usuario",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=500,y=100)

        etr_user = ttk.Entry(body,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
        etr_user.place(x=420,y=160)

        label = Label(body, text="Contraseña",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=480,y=220)

        etr_pas = ttk.Entry(body,width=20,font=font.Font(family="Arial",size=18),show="*",justify=CENTER)
        etr_pas.place(x=420,y=280)

        ingreso = ttk.Button(body,text="Ingresar",command=lambda: self.valid_ingreso(etr_user.get(),etr_pas.get()))
        ingreso.place(x=570,y=340,width=150,height=40)

        registro = ttk.Button(body,text="Registrar",command=lambda: self.intercabio_vista(inicio,"r"))
        registro.place(x=390,y=340,width=150,height=40)
    
    def create_register(self):
        self.master.configure(bg="#90B000")

        registro = Frame(self.master)
        registro.place(x=0, y=0, width=1200,height=900)

        header = Frame(registro, bg="green")
        header.place(x=0,y=0,height=200,width=1200)

        label = Label(header, image=self.img_header_inicio,bg="#90B000",fg="black",font=("Arial",22))
        label.place(x=0,y=0)

        body = Frame(registro, bg="#f3e7cc")
        body.place(x=0,y=200,height=680,width=1200)

        label = Label(body, text="Usuario",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=500,y=60)

        etr_user = ttk.Entry(body,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
        etr_user.place(x=420,y=110)

        label = Label(body, text="Contraseña",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=480,y=170)

        etr_pas = ttk.Entry(body,width=20,font=font.Font(family="Arial",size=18),show="*",justify=CENTER)
        etr_pas.place(x=420,y=230)

        label = Label(body, text="Repetir Contraseña",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=425,y=290)

        etr_pas_re = ttk.Entry(body,width=20,font=font.Font(family="Arial",size=18),show="*",justify=CENTER)
        etr_pas_re.place(x=420,y=350)

        registrar = ttk.Button(body,text="Registrar",command=lambda: self.valid_registro(etr_user.get(),etr_pas.get(),etr_pas_re.get(),registro))
        registrar.place(x=570,y=410,width=150,height=40)

        inicio = ttk.Button(body,text="Inicio",command=lambda: self.intercabio_vista(inicio,"i"))
        inicio.place(x=390,y=410,width=150,height=40)

