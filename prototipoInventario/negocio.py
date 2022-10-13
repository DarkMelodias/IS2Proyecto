from usuarios import *
from laboratorios import *
from materiales import *
from equipos import *

users = Usuarios()
labs = Laboratorios()
mats = Materiales()
equips = Equipos()

def ingreso(user,password):
    usuario = users.buscar_usuario(user)
    if usuario != None:
        if usuario[1] == password:
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