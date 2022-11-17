from usuarios import *
from laboratorios import *
from materiales import *
from equipos import *
from reserva import*

users = Usuarios()
labs = Laboratorios()
mats = Materiales()
equips = Equipos()
reserva = Reservas()


usr = ""
mater = 0
equip = 0

def ingreso(user,password):
    global usr
    usuario = users.buscar_usuario(user)
    if usuario != None:
        if usuario[1] == password:
            usr = usuario[0]
            return True
        else:
            return False
    else:
        return False

def registrar(user,password):
    registro = users.insertar_usuario(user, password)
    if registro == False:
        return False
    else:
        return True

def rlab(num,name,cap):
    registro = labs.insertar_laboratorios(num, name, cap)
    if registro == False:
        return False
    else:
        return True

def blab(num):
    busqueda = labs.buscar_laboratorio(num)
    if busqueda == None:
        return False
    else:
        return busqueda

def alab(num,name,cap):
    actualizacion = labs.modifica_laboratorio(num,name,cap)
    if actualizacion == False:
        return False
    else:
        return True

def elab(num):
    eliminacion = labs.eliminar_laboratorio(num)
    if eliminacion == False:
        return False
    else:
        return True

def rmat(num,name,cap):
    registro = mats.insertar_materiales(num, name, cap)
    if registro == False:
        return False
    else:
        return True

def bmat(num):
    busqueda = mats.buscar_materiales(num)
    if busqueda == None:
        return False
    else:
        return busqueda

def amat(num,name,cap):
    actualizacion = mats.modifica_materiales(num,name,cap)
    if actualizacion == False:
        return False
    else:
        return True

def emat(num):
    eliminacion = mats.eliminar_materiales(num)
    if eliminacion == False:
        return False
    else:
        return True

def requip(num,name,cap,est):
    registro = equips.insertar_equipos(num, name, cap, est)
    if registro == False:
        return False
    else:
        return True

def bequip(num):
    busqueda = equips.buscar_equipos(num)
    if busqueda == None:
        return False
    else:
        return busqueda

def aequip(num,name,cap,est):
    actualizacion = equips.modifica_equipos(num,name,cap,est)
    if actualizacion == False:
        return False
    else:
        return True

def eequip(num):
    eliminacion = equips.eliminar_equipos(num)
    if eliminacion == False:
        return False
    else:
        return True

def llenarMateriales():
    mat = []
    mat.clear()
    mat = mats.consulta_materialesN()
    equp = equips.consulta_equiposN()
    labos = labs.consulta_laboratorios()
    return mat,equp,labos

def gd_mat(mat):
    global mater
    rs = mats.buscar_materialesN(mat)
    mater = rs[0]

def gd_equip(mat):
    global equip
    if mat[0] == "{":
        mat = mat[1:-1]
    rs = equips.buscar_equiposN(mat)
    equip = rs[0]

def rreser(mates,equips,fecha,hora,lab):
    global usr
    reser = reserva.insertar_reserva(mates,equips,fecha,hora,lab,mater,equip,usr)
    if reser == False:
        return False
    else:
        return True

def bsreserva():
    rs = reserva.consulta_reservaS()
    return rs

def bpreserva(num):
    rs = reserva.buscar_reserva(num)
    busqueda = labs.buscar_laboratorio(rs[5])
    return rs,busqueda[1]

def ereser(num):
    eliminacion = reserva.eliminar_reserva(num)
    if eliminacion == False:
        return False
    else:
        return True

def bereserva(date_one,date_two):
    rs = reserva.busqueda_entre(date_one,date_two)
    return rs
