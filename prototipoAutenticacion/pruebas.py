import unittest

from usuarios import *

users = Usuarios()

usuario = "admin"
password = "1234"
class User(unittest.TestCase):
    def test_Inicio_Sesion(self):
        pass

# cuentas = users.consulta_usuarios()
# print(cuentas)

# busqueda = users.buscar_usuario(usuario)
# print(busqueda)

# users.insertar_usuario(usuario, password)

# a = hashlib.sha1(busqueda[1]).hexdigest()
# print(a)