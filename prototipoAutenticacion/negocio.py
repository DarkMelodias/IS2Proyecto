from usuarios import *

users = Usuarios()

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
