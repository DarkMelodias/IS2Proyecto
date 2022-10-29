from reserva import *
from laboratorios import *
from materiales import *
from equipos import *
from datetime import datetime
from usuarios import *

users = Usuarios()


rsvs = Reservas()
mates = Materiales()
equipos = Equipos()
labs = Laboratorios()


mats = []

mats.append(mates.buscar_materiales(1))
mats.append(mates.buscar_materiales(2))

mat = mats[0][0]


mate = ""
for element in mats:
    mate = mate+"{},".format(element[1])



equips = []
equips.append(equipos.buscar_equipos(1))
equips.append(equipos.buscar_equipos(2))

eq = equips[0][0]


equi = ""

for element in equips:
    equi = equi+"{},".format(element[1])


lab = labs.buscar_laboratorio(2)
lab = lab[0]


user = "admin"

# rsvs.insertar_reserva(mate,equi,fecha,lab,mat,eq,user)

rs = rsvs.buscar_reserva(4)
print(rs[3])
