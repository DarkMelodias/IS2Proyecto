from tkinter import *
from tkinter import ttk,font
import tkinter as tk
from usuarios import *
from negocio import *
from tkinter import messagebox
from view_inicio import *
from materiales import *
from tkcalendar import Calendar 

class Interfaz_inicio(Frame):

    def __init__(self,master,parent):
        super().__init__(master)
        self.master = master
        self.parent = parent
        ancho_ventana = 1200
        alto_ventana = 900

        x_ventana = self.master.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.master.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.master.geometry(posicion)

        self.img_header_inicio = tk.PhotoImage(file="pic/inicio_header.png")

        self.mate = ""
        self.equip = ""

        self.master.resizable(0,0)
        self.create_init()

    def act_lista(self):
        self.cont = 0
        self.materiales,self.equipos,self.laboratorios = llenarMateriales()
        self.reservas = bsreserva()

    def escribaFecha(self,event):
        if event.char.isdigit():
            texto = self.etr_hora.get()
            letras = 0
            for i in texto:
                letras +=1
            if letras == 2:
                self.etr_hora.insert(2,":")
            elif letras == 5:
                self.etr_hora.insert(5,":")
        else:
            return "break"

    def obtener_fecha(self): 
        dat = self.cal.get_date()
        dat = dat.split("/")
        dater = dat[2]+"/"+dat[1]+"/"+dat[0]

        self.etr_fecha.config(state=tk.NORMAL)
        self.etr_fecha.delete(0,END)
        self.etr_fecha.insert(0,dater)
        self.etr_fecha.config(state=tk.DISABLED)

    def llenaEntryMateriales(self,mat):
        gd_mat(mat)
        self.mate = self.mate+"{},".format(mat)
        self.etr_mate.config(state=tk.NORMAL)
        self.etr_mate.delete(0,END)
        self.etr_mate.insert(0,self.mate)
        self.etr_mate.config(state=tk.DISABLED)

    def llenaEntryEquipos(self,mat):
        gd_equip(mat)
        self.equip = self.equip+"{},".format(mat)
        self.etr_equip.config(state=tk.NORMAL)
        self.etr_equip.delete(0,END)
        self.etr_equip.insert(0,self.equip)
        self.etr_equip.config(state=tk.DISABLED)

    def limpiar(self):
        self.equip = ""
        self.mate = ""

    def cerrar_sesion(self):
        self.master.destroy()
        self.parent.deiconify()

    def intercabio_vista(self,esconde,muestra):
        esconde.place_forget()
        if muestra == "i":
            self.create_init()
        if muestra == "l":
            self.create_lab()
        if muestra == "m":
            self.create_mat()
        if muestra == "e":
            self.create_equip()
        if muestra == "r":
            self.create_res()
        if muestra == "c":
            pass

    def inter_lab(self,esconde,muestra):
        esconde.place_forget()
        if muestra == "r":
            self.reg_lab()
        if muestra == "a":
            self.act_lab()
        if muestra == "e":
            self.eli_lab()
        if muestra == 'l':
            self.create_lab()
    
    def inter_mat(self,esconde,muestra):
        esconde.place_forget()
        if muestra == "r":
            self.reg_mat()
        if muestra == "a":
            self.act_mat()
        if muestra == "e":
            self.eli_mat()
        if muestra == 'l':
            self.create_mat()

    def inter_equip(self,esconde,muestra):
        esconde.place_forget()
        if muestra == "r":
            self.reg_equip()
        if muestra == "a":
            self.act_equip()
        if muestra == "e":
            self.eli_equip()
        if muestra == 'l':
            self.create_equip()
    
    def inter_res(self,esconde,muestra):
        esconde.place_forget()
        if muestra == "r":
            self.reg_res()
        if muestra == "e":
            self.eli_res()
        if muestra == 'l':
            self.limpiar()
            self.create_res()

    def vr_lab(self,num,name,cap,r):
        valid = rlab(num,name,cap)
        if valid == True:
            messagebox.showinfo("Registro","Registro correcto")
            self.intercabio_vista(r,"l")
        else:
            messagebox.showerror("Registro","Registro incorrecto,laboratorio ya existe")

    def vr_mat(self,num,name,cap,r):
        valid = rmat(num,name,cap)
        if valid == True:
            messagebox.showinfo("Registro","Registro correcto")
            self.intercabio_vista(r,"m")
        else:
            messagebox.showerror("Registro","Registro incorrecto,material ya existe")

    def vr_equip(self,num,name,cap,est,r):
        valid = requip(num,name,cap,est)
        if valid == True:
            messagebox.showinfo("Registro","Registro correcto")
            self.intercabio_vista(r,"e")
        else:
            messagebox.showerror("Registro","Registro incorrecto, equipo ya existe")

    def vr_res(self,r):
        lab = self.etr_laboratorio.get()
        labf = lab.split(" ")
        labff = labf[0]
        valid =rreser(self.etr_mate.get(),self.etr_equip.get(),self.etr_fecha.get(),self.etr_hora.get(),labff)
        if valid == True:
            messagebox.showinfo("Registro","Registro correcto")
            self.intercabio_vista(r,"r")
        else:
            messagebox.showerror("Registro","Registro incorrecto, equipo ya existe")

    def va_lab(self,num,name,cap,r):
        valid = alab(num,name,cap)
        if valid == True:
            messagebox.showinfo("Actualización","Actualización correcta")
            self.intercabio_vista(r,"l")
        else:
            messagebox.showerror("Actualización","Actualización incorrecta")

    def va_mat(self,num,name,cap,r):
        valid = amat(num,name,cap)
        if valid == True:
            messagebox.showinfo("Actualización","Actualización correcta")
            self.intercabio_vista(r,"m")
        else:
            messagebox.showerror("Actualización","Actualización incorrecta")
    
    def va_equip(self,num,name,cap,est,r):
        valid = aequip(num,name,cap,est)
        if valid == True:
            messagebox.showinfo("Actualización","Actualización correcta")
            self.intercabio_vista(r,"e")
        else:
            messagebox.showerror("Actualización","Actualización incorrecta")

    def ve_lab(self,num,r):
        valid = elab(num)
        if valid == True:
            messagebox.showinfo("Eliminación","Eliminación correcta")
            self.intercabio_vista(r,"l")
        else:
            messagebox.showerror("Eliminación","Eliminación incorrecta")
    
    def ve_mat(self,num,r):
        valid = emat(num)
        if valid == True:
            messagebox.showinfo("Eliminación","Eliminación correcta")
            self.intercabio_vista(r,"m")
        else:
            messagebox.showerror("Eliminación","Eliminación incorrecta")

    def ve_equip(self,num,r):
        valid = eequip(num)
        if valid == True:
            messagebox.showinfo("Eliminación","Eliminación correcta")
            self.intercabio_vista(r,"e")
        else:
            messagebox.showerror("Eliminación","Eliminación incorrecta")
    
    def ve_res(self,num,r):
        valid = ereser(num)
        if valid == True:
            messagebox.showinfo("Eliminación","Eliminación correcta")
            self.intercabio_vista(r,"r")
        else:
            messagebox.showerror("Eliminación","Eliminación incorrecta")

    def reg_lab(self):
        lab = Frame(self.master)
        lab.place(x=0, y=0, width=1200,height=900)

        header = Frame(lab, bg="green")
        header.place(x=0,y=0,height=200,width=1200)

        label = Label(header, image=self.img_header_inicio,bg="#90B000",fg="black",font=("Arial",22))
        label.place(x=0,y=0)

        body = Frame(lab, bg="#f3e7cc")
        body.place(x=0,y=200,height=680,width=1200)

        label = Label(body, text="Registro Laboratorios",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=410,y=60)

        label = Label(body, text="Numero Laboratorio",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=418,y=160)

        etr_num = ttk.Entry(body,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
        etr_num.place(x=420,y=230)

        label = Label(body, text="Nombre Laboratorio",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=418,y=290)

        etr_name = ttk.Entry(body,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
        etr_name.place(x=420,y=350)

        label = Label(body, text="Capacidad",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=480,y=410)

        etr_cap = ttk.Entry(body,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
        etr_cap.place(x=420,y=470)

        registrar = ttk.Button(body,text="Registrar",command=lambda: self.vr_lab(etr_num.get(),etr_name.get(),etr_cap.get(),lab))
        registrar.place(x=570,y=530,width=150,height=40)

        inicio = ttk.Button(body,text="Volver",command=lambda: self.inter_lab(lab,"l"))
        inicio.place(x=390,y=530,width=150,height=40)

    def reg_mat(self):
        mat = Frame(self.master)
        mat.place(x=0, y=0, width=1200,height=900)

        header = Frame(mat, bg="green")
        header.place(x=0,y=0,height=200,width=1200)

        label = Label(header, image=self.img_header_inicio,bg="#90B000",fg="black",font=("Arial",22))
        label.place(x=0,y=0)

        body = Frame(mat, bg="#f3e7cc")
        body.place(x=0,y=200,height=680,width=1200)

        label = Label(body, text="Registro Materiales",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=410,y=60)

        label = Label(body, text="Codigo Material",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=418,y=160)

        etr_num = ttk.Entry(body,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
        etr_num.place(x=420,y=230)

        label = Label(body, text="Nombre Material",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=418,y=290)

        etr_name = ttk.Entry(body,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
        etr_name.place(x=420,y=350)

        label = Label(body, text="Cantidad",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=480,y=410)

        etr_cap = ttk.Entry(body,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
        etr_cap.place(x=420,y=470)

        registrar = ttk.Button(body,text="Registrar",command=lambda: self.vr_mat(etr_num.get(),etr_name.get(),etr_cap.get(),mat))
        registrar.place(x=570,y=530,width=150,height=40)

        inicio = ttk.Button(body,text="Volver",command=lambda: self.inter_mat(mat,"l"))
        inicio.place(x=390,y=530,width=150,height=40)

    def reg_equip(self):
        equip = Frame(self.master)
        equip.place(x=0, y=0, width=1200,height=900)

        header = Frame(equip, bg="green")
        header.place(x=0,y=0,height=200,width=1200)

        label = Label(header, image=self.img_header_inicio,bg="#90B000",fg="black",font=("Arial",22))
        label.place(x=0,y=0)

        body = Frame(equip, bg="#f3e7cc")
        body.place(x=0,y=200,height=680,width=1200)

        label = Label(body, text="Registro Equipos",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=440,y=20)

        label = Label(body, text="Codigo Equipos",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=448,y=90)

        etr_num = ttk.Entry(body,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
        etr_num.place(x=420,y=160)

        label = Label(body, text="Nombre Equipos",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=448,y=220)

        etr_name = ttk.Entry(body,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
        etr_name.place(x=420,y=280)

        label = Label(body, text="Cantidad",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=495,y=340)

        etr_cap = ttk.Entry(body,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
        etr_cap.place(x=420,y=400)

        label = Label(body, text="Estado",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=505,y=460)

        etr_est = ttk.Entry(body,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
        etr_est.place(x=420,y=520)

        registrar = ttk.Button(body,text="Registrar",command=lambda: self.vr_equip(etr_num.get(),etr_name.get(),etr_cap.get(),etr_est.get(),equip))
        registrar.place(x=570,y=620,width=150,height=40)

        inicio = ttk.Button(body,text="Volver",command=lambda: self.inter_equip(equip,"l"))
        inicio.place(x=390,y=620,width=150,height=40)

    def reg_res(self):
        self.act_lista()
        res = Frame(self.master)
        res.place(x=0, y=0, width=1200,height=900)

        header = Frame(res, bg="green")
        header.place(x=0,y=0,height=200,width=1200)

        label = Label(header, image=self.img_header_inicio,bg="#90B000",fg="black",font=("Arial",22))
        label.place(x=0,y=0)

        body = Frame(res, bg="#f3e7cc")
        body.place(x=0,y=200,height=680,width=1200)

        label = Label(body, text="Registro Reservas",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=440,y=20)

        label = Label(body, text="Materiales",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=193,y=90)

        self.act_lista()
        cbx_mate = ttk.Combobox(body,width=18,font=font.Font(family="Arial",size=19),justify=CENTER,values=self.materiales,state="readonly")
        cbx_mate.place(x=120,y=160)

        btn_mate = ttk.Button(body,text="Añadir",command=lambda:self.llenaEntryMateriales(cbx_mate.get()))
        btn_mate.place(x=420,y=160,height=40)

        self.etr_mate = ttk.Entry(body,width=40,font=font.Font(family="Arial",size=18),justify=CENTER)
        self.etr_mate.config(state=tk.DISABLED)
        self.etr_mate.place(x=520,y=160)

        label = Label(body, text="Equipos",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=195,y=220)

        cbx_equip = ttk.Combobox(body,width=18,font=font.Font(family="Arial",size=19),justify=CENTER,values=self.equipos,state="readonly")
        cbx_equip.place(x=120,y=280)

        btn_equip = ttk.Button(body,text="Añadir",command=lambda:self.llenaEntryEquipos(cbx_equip.get()))
        btn_equip.place(x=420,y=280,height=40)

        self.etr_equip = ttk.Entry(body,width=40,font=font.Font(family="Arial",size=18),justify=CENTER)
        self.etr_equip.config(state=tk.DISABLED)
        self.etr_equip.place(x=520,y=280)

        label = Label(body, text="Calendario",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=195,y=340)

        self.cal = Calendar(body, selectmode = 'day', year = 2022, month = 10, day = 11) 
        self.cal.place(x=120,y=400)
        
        btn_equip = ttk.Button(body,text="Añadir",command=self.obtener_fecha)
        btn_equip.place(x=420,y=400,height=40)

        self.etr_fecha = ttk.Entry(body,width=40,font=font.Font(family="Arial",size=18),justify=CENTER)
        self.etr_fecha.config(state=tk.DISABLED)
        self.etr_fecha.place(x=520,y=400)

        label = Label(body, text="Hora: ",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=420,y=450)

        self.etr_hora = ttk.Entry(body,width=40,font=font.Font(family="Arial",size=18),justify=CENTER)
        self.etr_hora.place(x=520,y=460)

        label = Label(body, text="Laboratorio: ",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=420,y=520)

        self.etr_laboratorio = ttk.Combobox(body,width=18,font=font.Font(family="Arial",size=19),justify=CENTER,values=self.laboratorios,state="readonly")
        self.etr_laboratorio.place(x=600,y=520)

        self.etr_hora.bind("<Key>", self.escribaFecha)
        self.etr_hora.bind("<BackSpace>", lambda _:self.etr_hora.delete(tk.END))

        registrar = ttk.Button(body,text="Registrar",command=lambda:self.vr_res(res))
        registrar.place(x=570,y=620,width=150,height=40)

        inicio = ttk.Button(body,text="Volver",command=lambda: self.inter_res(res,"l"))
        inicio.place(x=390,y=620,width=150,height=40)

    def vb_lab(self,num,lab):
        datos = blab(num)
        if datos != False:
            bodyR = Frame(lab, bg="#f3e7cc")
            bodyR.place(x=400,y=200,height=680,width=800)

            label = Label(bodyR, text="Actualizacion Laboratorios",bg="#f3e7cc",fg="black",font=("Arial",22))
            label.place(x=295,y=60)

            label = Label(bodyR, text="Numero Laboratorio",bg="#f3e7cc",fg="black",font=("Arial",22))
            label.place(x=318,y=160)

            etr_num = ttk.Entry(bodyR,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
            etr_num.insert(0,datos[0])
            etr_num.config(state=tk.DISABLED)
            etr_num.place(x=320,y=230)

            label = Label(bodyR, text="Nombre Laboratorio",bg="#f3e7cc",fg="black",font=("Arial",22))
            label.place(x=318,y=290)

            etr_name = ttk.Entry(bodyR,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
            etr_name.insert(0,datos[1])
            etr_name.place(x=320,y=350)

            label = Label(bodyR, text="Capacidad",bg="#f3e7cc",fg="black",font=("Arial",22))
            label.place(x=380,y=410)

            etr_cap = ttk.Entry(bodyR,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
            etr_cap.insert(0,datos[2])
            etr_cap.place(x=320,y=470)

            actualizar = ttk.Button(bodyR,text="Actualizar",command=lambda: self.va_lab(etr_num.get(),etr_name.get(),etr_cap.get(),lab))
            actualizar.place(x=460,y=560,width=150,height=40)

            cancelar = ttk.Button(bodyR,text="Cancelar",command=lambda: self.inter_lab(bodyR,"a"))
            cancelar.place(x=280,y=560,width=150,height=40)

        else:
            messagebox.showerror("Busqueda","Busqueda incorrecta, laboratorio no existe")
    
    def vb_mat(self,num,mat):
        datos = bmat(num)
        if datos != False:
            bodyR = Frame(mat, bg="#f3e7cc")
            bodyR.place(x=400,y=200,height=680,width=800)

            label = Label(bodyR, text="Actualizacion Materiales",bg="#f3e7cc",fg="black",font=("Arial",22))
            label.place(x=295,y=60)

            label = Label(bodyR, text="Codigo Material",bg="#f3e7cc",fg="black",font=("Arial",22))
            label.place(x=318,y=160)

            etr_num = ttk.Entry(bodyR,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
            etr_num.insert(0,datos[0])
            etr_num.config(state=tk.DISABLED)
            etr_num.place(x=320,y=230)

            label = Label(bodyR, text="Nombre Material",bg="#f3e7cc",fg="black",font=("Arial",22))
            label.place(x=318,y=290)

            etr_name = ttk.Entry(bodyR,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
            etr_name.insert(0,datos[1])
            etr_name.place(x=320,y=350)

            label = Label(bodyR, text="Cantidad",bg="#f3e7cc",fg="black",font=("Arial",22))
            label.place(x=380,y=410)

            etr_cap = ttk.Entry(bodyR,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
            etr_cap.insert(0,datos[2])
            etr_cap.place(x=320,y=470)

            actualizar = ttk.Button(bodyR,text="Actualizar",command=lambda: self.va_mat(etr_num.get(),etr_name.get(),etr_cap.get(),mat))
            actualizar.place(x=460,y=560,width=150,height=40)

            cancelar = ttk.Button(bodyR,text="Cancelar",command=lambda: self.inter_mat(bodyR,"a"))
            cancelar.place(x=280,y=560,width=150,height=40)

        else:
            messagebox.showerror("Busqueda","Busqueda incorrecta, material no existe")

    def vb_equip(self,num,equip):
        datos = bequip(num)
        if datos != False:
            bodyR = Frame(equip, bg="#f3e7cc")
            bodyR.place(x=400,y=200,height=680,width=800)

            label = Label(bodyR, text="Actualizar Equipos",bg="#f3e7cc",fg="black",font=("Arial",22))
            label.place(x=340,y=20)

            label = Label(bodyR, text="Codigo Equipos",bg="#f3e7cc",fg="black",font=("Arial",22))
            label.place(x=348,y=90)

            etr_num = ttk.Entry(bodyR,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
            etr_num.insert(0,datos[0])
            etr_num.config(state=tk.DISABLED)
            etr_num.place(x=320,y=160)

            label = Label(bodyR, text="Nombre Equipos",bg="#f3e7cc",fg="black",font=("Arial",22))
            label.place(x=348,y=220)

            etr_name = ttk.Entry(bodyR,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
            etr_name.insert(0,datos[1])
            etr_name.place(x=320,y=280)

            label = Label(bodyR, text="Cantidad",bg="#f3e7cc",fg="black",font=("Arial",22))
            label.place(x=395,y=340)

            etr_cap = ttk.Entry(bodyR,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
            etr_cap.insert(0,datos[2])
            etr_cap.place(x=320,y=400)

            label = Label(bodyR, text="Estado",bg="#f3e7cc",fg="black",font=("Arial",22))
            label.place(x=305,y=460)

            etr_est = ttk.Entry(bodyR,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
            etr_est.insert(0,datos[3])
            etr_est.place(x=320,y=520)

            actualizar = ttk.Button(bodyR,text="Actualizar",command=lambda: self.va_equip(etr_num.get(),etr_name.get(),etr_cap.get(),etr_est.get(),equip))
            actualizar.place(x=460,y=620,width=150,height=40)

            cancelar = ttk.Button(bodyR,text="Cancelar",command=lambda: self.inter_equip(bodyR,"a"))
            cancelar.place(x=280,y=620,width=150,height=40)

        else:
            messagebox.showerror("Busqueda","Busqueda incorrecta, equipo no existe")

    def vbe_lab(self,num,lab):
        datos = blab(num)
        if datos != False:
            bodyR = Frame(lab, bg="#f3e7cc")
            bodyR.place(x=400,y=200,height=680,width=800)

            label = Label(bodyR, text="Actualizacion Laboratorios",bg="#f3e7cc",fg="black",font=("Arial",22))
            label.place(x=295,y=60)

            label = Label(bodyR, text="Numero Laboratorio",bg="#f3e7cc",fg="black",font=("Arial",22))
            label.place(x=318,y=160)

            etr_num = ttk.Entry(bodyR,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
            etr_num.insert(0,datos[0])
            etr_num.config(state=tk.DISABLED)
            etr_num.place(x=320,y=230)

            label = Label(bodyR, text="Nombre Laboratorio",bg="#f3e7cc",fg="black",font=("Arial",22))
            label.place(x=318,y=290)

            etr_name = ttk.Entry(bodyR,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
            etr_name.insert(0,datos[1])
            etr_name.config(state=tk.DISABLED)
            etr_name.place(x=320,y=350)

            label = Label(bodyR, text="Capacidad",bg="#f3e7cc",fg="black",font=("Arial",22))
            label.place(x=380,y=410)

            etr_cap = ttk.Entry(bodyR,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
            etr_cap.insert(0,datos[2])
            etr_cap.config(state=tk.DISABLED)
            etr_cap.place(x=320,y=470)

            actualizar = ttk.Button(bodyR,text="Eliminar",command=lambda: self.ve_lab(etr_num.get(),lab))
            actualizar.place(x=460,y=560,width=150,height=40)

            cancelar = ttk.Button(bodyR,text="Cancelar",command=lambda: self.inter_lab(bodyR,"e"))
            cancelar.place(x=280,y=560,width=150,height=40)

        else:
            messagebox.showerror("Busqueda","Busqueda incorrecta, laboratorio no existe")

    def vbe_mat(self,num,mat):
        datos = bmat(num)
        if datos != False:
            bodyR = Frame(mat, bg="#f3e7cc")
            bodyR.place(x=400,y=200,height=680,width=800)

            label = Label(bodyR, text="Actualizacion Materiales",bg="#f3e7cc",fg="black",font=("Arial",22))
            label.place(x=295,y=60)

            label = Label(bodyR, text="Numero Materiale",bg="#f3e7cc",fg="black",font=("Arial",22))
            label.place(x=318,y=160)

            etr_num = ttk.Entry(bodyR,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
            etr_num.insert(0,datos[0])
            etr_num.config(state=tk.DISABLED)
            etr_num.place(x=320,y=230)

            label = Label(bodyR, text="Nombre Materiale",bg="#f3e7cc",fg="black",font=("Arial",22))
            label.place(x=318,y=290)

            etr_name = ttk.Entry(bodyR,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
            etr_name.insert(0,datos[1])
            etr_name.config(state=tk.DISABLED)
            etr_name.place(x=320,y=350)

            label = Label(bodyR, text="Capacidad",bg="#f3e7cc",fg="black",font=("Arial",22))
            label.place(x=380,y=410)

            etr_cap = ttk.Entry(bodyR,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
            etr_cap.insert(0,datos[2])
            etr_cap.config(state=tk.DISABLED)
            etr_cap.place(x=320,y=470)

            actualizar = ttk.Button(bodyR,text="Eliminar",command=lambda: self.ve_mat(etr_num.get(),mat))
            actualizar.place(x=460,y=560,width=150,height=40)

            cancelar = ttk.Button(bodyR,text="Cancelar",command=lambda: self.inter_mat(bodyR,"e"))
            cancelar.place(x=280,y=560,width=150,height=40)

        else:
            messagebox.showerror("Busqueda","Busqueda incorrecta, material no existe")

    def vbe_equip(self,num,equip):
        datos = bequip(num)
        if datos != False:
            bodyR = Frame(equip, bg="#f3e7cc")
            bodyR.place(x=400,y=200,height=680,width=800)

            label = Label(bodyR, text="Eliminar Equipos",bg="#f3e7cc",fg="black",font=("Arial",22))
            label.place(x=340,y=20)

            label = Label(bodyR, text="Codigo Equipos",bg="#f3e7cc",fg="black",font=("Arial",22))
            label.place(x=348,y=90)

            etr_num = ttk.Entry(bodyR,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
            etr_num.insert(0,datos[0])
            etr_num.config(state=tk.DISABLED)
            etr_num.place(x=320,y=160)

            label = Label(bodyR, text="Nombre Equipos",bg="#f3e7cc",fg="black",font=("Arial",22))
            label.place(x=348,y=220)

            etr_name = ttk.Entry(bodyR,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
            etr_name.insert(0,datos[1])
            etr_name.config(state=tk.DISABLED)
            etr_name.place(x=320,y=280)

            label = Label(bodyR, text="Cantidad",bg="#f3e7cc",fg="black",font=("Arial",22))
            label.place(x=395,y=340)

            etr_cap = ttk.Entry(bodyR,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
            etr_cap.insert(0,datos[2])
            etr_cap.config(state=tk.DISABLED)
            etr_cap.place(x=320,y=400)

            label = Label(bodyR, text="Estado",bg="#f3e7cc",fg="black",font=("Arial",22))
            label.place(x=305,y=460)

            etr_est = ttk.Entry(bodyR,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
            etr_est.insert(0,datos[3])
            etr_est.config(state=tk.DISABLED)
            etr_est.place(x=320,y=520)

            actualizar = ttk.Button(bodyR,text="Eliminar",command=lambda: self.ve_equip(etr_num.get(),equip))
            actualizar.place(x=460,y=620,width=150,height=40)

            cancelar = ttk.Button(bodyR,text="Cancelar",command=lambda: self.inter_equip(bodyR,"e"))
            cancelar.place(x=280,y=620,width=150,height=40)

        else:
            messagebox.showerror("Busqueda","Busqueda incorrecta, equipo no existe")

    def vbe_res(self,date,equip):

        dat = date.split(" ")
        ide = dat[0]
        datos,lab = bpreserva(ide)
        bodyR = Frame(equip, bg="#f3e7cc")
        bodyR.place(x=400,y=200,height=680,width=800)

        label = Label(bodyR, text="Eliminar Reservas",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=340,y=20)

        label = Label(bodyR, text="Laboratorio",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=348,y=90)

        etr_num = ttk.Entry(bodyR,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
        etr_num.insert(0,lab)
        etr_num.config(state=tk.DISABLED)
        etr_num.place(x=320,y=160)

        label = Label(bodyR, text="Fecha",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=348,y=220)

        etr_name = ttk.Entry(bodyR,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
        etr_name.insert(0,datos[3])
        etr_name.config(state=tk.DISABLED)
        etr_name.place(x=320,y=280)

        label = Label(bodyR, text="Hora",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=395,y=340)

        etr_cap = ttk.Entry(bodyR,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
        etr_cap.insert(0,datos[4])
        etr_cap.config(state=tk.DISABLED)
        etr_cap.place(x=320,y=400)

        actualizar = ttk.Button(bodyR,text="Eliminar",command=lambda: self.ve_res(dat[0],equip))
        actualizar.place(x=460,y=620,width=150,height=40)

        cancelar = ttk.Button(bodyR,text="Cancelar",command=lambda: self.inter_res(bodyR,"e"))
        cancelar.place(x=280,y=620,width=150,height=40)

    def act_lab(self):
        lab = Frame(self.master, bg="#f3e7cc")
        lab.place(x=0, y=0, width=1200,height=900)

        header = Frame(lab, bg="green")
        header.place(x=0,y=0,height=200,width=1200)

        label = Label(header, image=self.img_header_inicio,bg="#90B000",fg="black",font=("Arial",22))
        label.place(x=0,y=0)

        bodyL = Frame(lab, bg="#f3e7cc")
        bodyL.place(x=0,y=200,height=680,width=400)

        label = Label(bodyL, text="Busqueda Laboratorios",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=72,y=60)

        label = Label(bodyL, text="Numero Laboratorio",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=76,y=160)

        etr_num = ttk.Entry(bodyL,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
        etr_num.place(x=70,y=230)

        busqueda = ttk.Button(bodyL,text="Buscar",command=lambda: self.vb_lab(etr_num.get(),lab))
        busqueda.place(x=120,y=480,width=150,height=40)

        inicio = ttk.Button(bodyL,text="Volver",command=lambda: self.inter_lab(lab,"l"))
        inicio.place(x=120,y=530,width=150,height=40)

    def act_mat(self):
        mat = Frame(self.master, bg="#f3e7cc")
        mat.place(x=0, y=0, width=1200,height=900)

        header = Frame(mat, bg="green")
        header.place(x=0,y=0,height=200,width=1200)

        label = Label(header, image=self.img_header_inicio,bg="#90B000",fg="black",font=("Arial",22))
        label.place(x=0,y=0)

        bodyL = Frame(mat, bg="#f3e7cc")
        bodyL.place(x=0,y=200,height=680,width=400)

        label = Label(bodyL, text="Busqueda Materiales",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=72,y=60)

        label = Label(bodyL, text="Codigo Material",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=76,y=160)

        etr_num = ttk.Entry(bodyL,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
        etr_num.place(x=70,y=230)

        busqueda = ttk.Button(bodyL,text="Buscar",command=lambda: self.vb_mat(etr_num.get(),mat))
        busqueda.place(x=120,y=480,width=150,height=40)

        inicio = ttk.Button(bodyL,text="Volver",command=lambda: self.inter_mat(mat,"l"))
        inicio.place(x=120,y=530,width=150,height=40)

    def act_equip(self):
        equip = Frame(self.master, bg="#f3e7cc")
        equip.place(x=0, y=0, width=1200,height=900)

        header = Frame(equip, bg="green")
        header.place(x=0,y=0,height=200,width=1200)

        label = Label(header, image=self.img_header_inicio,bg="#90B000",fg="black",font=("Arial",22))
        label.place(x=0,y=0)

        bodyL = Frame(equip, bg="#f3e7cc")
        bodyL.place(x=0,y=200,height=680,width=400)

        label = Label(bodyL, text="Busqueda Equipo",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=72,y=60)

        label = Label(bodyL, text="Codigo Equipo",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=76,y=160)

        etr_num = ttk.Entry(bodyL,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
        etr_num.place(x=70,y=230)

        busqueda = ttk.Button(bodyL,text="Buscar",command=lambda: self.vb_equip(etr_num.get(),equip))
        busqueda.place(x=120,y=480,width=150,height=40)

        inicio = ttk.Button(bodyL,text="Volver",command=lambda: self.inter_equip(equip,"l"))
        inicio.place(x=120,y=530,width=150,height=40)

    def eli_lab(self):
        lab = Frame(self.master, bg="#f3e7cc")
        lab.place(x=0, y=0, width=1200,height=900)

        header = Frame(lab, bg="green")
        header.place(x=0,y=0,height=200,width=1200)

        label = Label(header, image=self.img_header_inicio,bg="#90B000",fg="black",font=("Arial",22))
        label.place(x=0,y=0)

        bodyL = Frame(lab, bg="#f3e7cc")
        bodyL.place(x=0,y=200,height=680,width=400)

        label = Label(bodyL, text="Busqueda Laboratorios",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=72,y=60)

        label = Label(bodyL, text="Numero Laboratorio",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=76,y=160)

        etr_num = ttk.Entry(bodyL,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
        etr_num.place(x=70,y=230)

        busqueda = ttk.Button(bodyL,text="Buscar",command=lambda: self.vbe_lab(etr_num.get(),lab))
        busqueda.place(x=120,y=480,width=150,height=40)

        inicio = ttk.Button(bodyL,text="Volver",command=lambda: self.inter_lab(lab,"l"))
        inicio.place(x=120,y=530,width=150,height=40)

    def eli_mat(self):
        mat = Frame(self.master, bg="#f3e7cc")
        mat.place(x=0, y=0, width=1200,height=900)

        header = Frame(mat, bg="green")
        header.place(x=0,y=0,height=200,width=1200)

        label = Label(header, image=self.img_header_inicio,bg="#90B000",fg="black",font=("Arial",22))
        label.place(x=0,y=0)

        bodyL = Frame(mat, bg="#f3e7cc")
        bodyL.place(x=0,y=200,height=680,width=400)

        label = Label(bodyL, text="Busqueda Materiales",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=72,y=60)

        label = Label(bodyL, text="Codigo Material",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=76,y=160)

        etr_num = ttk.Entry(bodyL,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
        etr_num.place(x=70,y=230)

        busqueda = ttk.Button(bodyL,text="Buscar",command=lambda: self.vbe_mat(etr_num.get(),mat))
        busqueda.place(x=120,y=480,width=150,height=40)

        inicio = ttk.Button(bodyL,text="Volver",command=lambda: self.inter_mat(mat,"l"))
        inicio.place(x=120,y=530,width=150,height=40)

    def eli_equip(self):
        equip = Frame(self.master, bg="#f3e7cc")
        equip.place(x=0, y=0, width=1200,height=900)

        header = Frame(equip, bg="green")
        header.place(x=0,y=0,height=200,width=1200)

        label = Label(header, image=self.img_header_inicio,bg="#90B000",fg="black",font=("Arial",22))
        label.place(x=0,y=0)

        bodyL = Frame(equip, bg="#f3e7cc")
        bodyL.place(x=0,y=200,height=680,width=400)

        label = Label(bodyL, text="Busqueda Equipos",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=72,y=60)

        label = Label(bodyL, text="Codigo Equipo",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=76,y=160)

        etr_num = ttk.Entry(bodyL,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
        etr_num.place(x=70,y=230)

        busqueda = ttk.Button(bodyL,text="Buscar",command=lambda: self.vbe_equip(etr_num.get(),equip))
        busqueda.place(x=120,y=480,width=150,height=40)

        inicio = ttk.Button(bodyL,text="Volver",command=lambda: self.inter_equip(equip,"l"))
        inicio.place(x=120,y=530,width=150,height=40)

    def eli_res(self):
        self.act_lista()
        res = Frame(self.master, bg="#f3e7cc")
        res.place(x=0, y=0, width=1200,height=900)

        header = Frame(res, bg="green")
        header.place(x=0,y=0,height=200,width=1200)

        label = Label(header, image=self.img_header_inicio,bg="#90B000",fg="black",font=("Arial",22))
        label.place(x=0,y=0)

        bodyL = Frame(res, bg="#f3e7cc")
        bodyL.place(x=0,y=200,height=680,width=400)

        label = Label(bodyL, text="Busqueda Reserva",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=72,y=60)

        label = Label(bodyL, text="Codigo Reserva",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=76,y=160)

        self.etr_reservas = ttk.Combobox(bodyL,width=20,font=font.Font(family="Arial",size=18),values=self.reservas,justify=CENTER)
        self.etr_reservas.place(x=70,y=230)

        busqueda = ttk.Button(bodyL,text="Buscar",command=lambda: self.vbe_res(self.etr_reservas.get(),res))
        busqueda.place(x=120,y=480,width=150,height=40)

        inicio = ttk.Button(bodyL,text="Volver",command=lambda: self.inter_res(res,"l"))
        inicio.place(x=120,y=530,width=150,height=40)

    def create_lab(self):
        lab = Frame(self.master)
        lab.place(x=0, y=0, width=1200,height=900)

        header = Frame(lab, bg="green")
        header.place(x=0,y=0,height=200,width=1200)

        label = Label(header, image=self.img_header_inicio,bg="#90B000",fg="black",font=("Arial",22))
        label.place(x=0,y=0)

        body = Frame(lab, bg="#f3e7cc")
        body.place(x=0,y=200,height=680,width=1200)

        label = Label(body, text="Laboratorios",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=500,y=60)

        registro = ttk.Button(body,text="Registro",command=lambda:self.inter_lab(lab,"r"))
        registro.place(x=400,y=200,width=150,height=40)

        actualizacion = ttk.Button(body,text="Actualizacion",command=lambda:self.inter_lab(lab,"a"))
        actualizacion.place(x=600,y=200,width=150,height=40)

        eliminar = ttk.Button(body,text="Eliminar",command=lambda:self.inter_lab(lab,"e"))
        eliminar.place(x=500,y=300,width=150,height=40)

        volver = ttk.Button(body,text="Volver",command=lambda:self.intercabio_vista(lab,"i"))
        volver.place(x=500,y=580,width=150,height=40)
        
    def create_mat(self):
        mat = Frame(self.master)
        mat.place(x=0, y=0, width=1200,height=900)

        header = Frame(mat, bg="green")
        header.place(x=0,y=0,height=200,width=1200)

        label = Label(header, image=self.img_header_inicio,bg="#90B000",fg="black",font=("Arial",22))
        label.place(x=0,y=0)

        body = Frame(mat, bg="#f3e7cc")
        body.place(x=0,y=200,height=680,width=1200)

        label = Label(body, text="Materiales",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=500,y=60)

        registro = ttk.Button(body,text="Registro",command=lambda:self.inter_mat(mat,"r"))
        registro.place(x=400,y=200,width=150,height=40)

        actualizacion = ttk.Button(body,text="Actualizacion",command=lambda:self.inter_mat(mat,"a"))
        actualizacion.place(x=600,y=200,width=150,height=40)

        eliminar = ttk.Button(body,text="Eliminar",command=lambda:self.inter_mat(mat,"e"))
        eliminar.place(x=500,y=300,width=150,height=40)

        volver = ttk.Button(body,text="Volver",command=lambda:self.intercabio_vista(mat,"i"))
        volver.place(x=500,y=580,width=150,height=40)

    def create_equip(self):
        equip = Frame(self.master)
        equip.place(x=0, y=0, width=1200,height=900)

        header = Frame(equip, bg="green")
        header.place(x=0,y=0,height=200,width=1200)

        label = Label(header, image=self.img_header_inicio,bg="#90B000",fg="black",font=("Arial",22))
        label.place(x=0,y=0)

        body = Frame(equip, bg="#f3e7cc")
        body.place(x=0,y=200,height=680,width=1200)

        label = Label(body, text="Equipos",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=500,y=60)

        registro = ttk.Button(body,text="Registro",command=lambda:self.inter_equip(equip,"r"))
        registro.place(x=400,y=200,width=150,height=40)

        actualizacion = ttk.Button(body,text="Actualizacion",command=lambda:self.inter_equip(equip,"a"))
        actualizacion.place(x=600,y=200,width=150,height=40)

        eliminar = ttk.Button(body,text="Eliminar",command=lambda:self.inter_equip(equip,"e"))
        eliminar.place(x=500,y=300,width=150,height=40)

        volver = ttk.Button(body,text="Volver",command=lambda:self.intercabio_vista(equip,"i"))
        volver.place(x=500,y=580,width=150,height=40)

    def create_res(self):
        self.act_lista()
        res = Frame(self.master)
        res.place(x=0, y=0, width=1200,height=900)

        header = Frame(res, bg="green")
        header.place(x=0,y=0,height=200,width=1200)

        label = Label(header, image=self.img_header_inicio,bg="#90B000",fg="black",font=("Arial",22))
        label.place(x=0,y=0)

        body = Frame(res, bg="#f3e7cc")
        body.place(x=0,y=200,height=680,width=1200)

        label = Label(body, text="Reservas",bg="#f3e7cc",fg="black",font=("Arial",22))
        label.place(x=500,y=60)

        registro = ttk.Button(body,text="Registro",command=lambda:self.inter_res(res,"r"))
        registro.place(x=400,y=200,width=150,height=40)

        eliminar = ttk.Button(body,text="Eliminar",command=lambda:self.inter_res(res,"e"))
        eliminar.place(x=600,y=200,width=150,height=40)

        volver = ttk.Button(body,text="Volver",command=lambda:self.intercabio_vista(res,"i"))
        volver.place(x=500,y=580,width=150,height=40)

    def create_init(self):

        self.master.configure(bg="#90B000")

        inicio = Frame(self.master)
        inicio.place(x=0, y=0, width=1200,height=900)

        header = Frame(inicio, bg="green")
        header.place(x=0,y=0,height=200,width=1200)

        label = Label(header, image=self.img_header_inicio,bg="#90B000",fg="black",font=("Arial",22))
        label.place(x=0,y=0)

        body = Frame(inicio, bg="#f3e7cc")
        body.place(x=0,y=200,height=680,width=1200)

        laboratorios = ttk.Button(body,text="Laboratorios",command=lambda:self.intercabio_vista(inicio,"l"))
        laboratorios.place(x=400,y=200,width=150,height=40)

        materiales = ttk.Button(body,text="Materiales", command=lambda:self.intercabio_vista(inicio,"m"))
        materiales.place(x=600,y=200,width=150,height=40)

        equipos = ttk.Button(body,text="Equipos", command=lambda:self.intercabio_vista(inicio,"e"))
        equipos.place(x=400,y=300,width=150,height=40)

        reserva = ttk.Button(body,text="Reserva", command=lambda:self.intercabio_vista(inicio,"r"))
        reserva.place(x=600,y=300,width=150,height=40)

        calendario = ttk.Button(body,text="Calendario")
        calendario.place(x=500,y=400,width=150,height=40)

        cerrar = ttk.Button(body,text="Cerrar Sesión",command=self.cerrar_sesion)
        cerrar.place(x=500,y=580,width=150,height=40)