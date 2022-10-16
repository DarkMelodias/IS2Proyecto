import mysql.connector

class Reservas:
    def __init__(self):
        #!!!!!!!!!!!!!!! importante cambiar la conexio a la base de datos
        self.cnn = mysql.connector.connect(host="localhost", user="root", passwd="samuel",database="is2proyecto") # cambiar cada que se haga un pull
    
    def __str__(self):
        datos = self.consulta_reserva()
        aux = ""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux

    def consulta_reserva(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM reservas")
        datos = cur.fetchall()
        if len(datos) == 0:
            cur.close()
            return None
        else:
            cur.close()
            return datos

    def consulta_reservaS(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT id_reserva,fecha,hora,Laboratorio_num_laboratorio FROM reservas")
        datos = cur.fetchall()
        if len(datos) == 0:
            cur.close()
            return None
        else:
            cur.close()
            return datos

    def buscar_reserva(self, num):
        cur = self.cnn.cursor()
        sql = "SELECT id_reserva, materiales, equipos, fecha, hora, Laboratorio_num_laboratorio FROM reservas WHERE id_reserva='{}' ".format(num)
        cur.execute(sql)
        datos = cur.fetchone()
        if datos == None:
            cur.close()
            return None
        else:
            cur.close()
            return datos

    def insertar_reserva(self,mate,equip,fecha,hora,lab,cod_mat,cod_equp,user):
        cur = self.cnn.cursor()
        sql = "INSERT INTO reservas (materiales, equipos, fecha,hora, Laboratorio_num_laboratorio, Materiales_cod_material, Equipos_cod_equipo, usuarios_user) VALUES('{}','{}',date_format('{}','%Y-%m-%\d'),'{}','{}','{}','{}','{}')".format(mate,equip,fecha,hora,lab,cod_mat,cod_equp,user)
        cur.execute(sql)
        n= cur.rowcount
        self.cnn.commit()
        cur.close()
        return True

    def eliminar_reserva(self,num):
        datos = self.buscar_reserva(num)
        if datos != None:
            cur = self.cnn.cursor()
            sql = "DELETE FROM reservas WHERE id_reserva = '{}'".format(num)
            cur.execute(sql)
            n=cur.rowcount
            self.cnn.commit()
            cur.close()
            return True
        else:
            return False 