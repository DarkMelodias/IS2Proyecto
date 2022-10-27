import mysql.connector


class Equipos:
    def __init__(self):
        #!!!!!!!!!!!!!!! importante cambiar la conexio a la base de datos
        self.cnn = mysql.connector.connect(host="localhost", user="root", passwd="guille",database="is2proyecto") # cambiar cada que se haga un pull
    
    def __str__(self):
        datos = self.consulta_equipos()
        aux = ""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux

    def consulta_equipos(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM equipos")
        datos = cur.fetchall()
        if len(datos) == 0:
            cur.close()
            return None
        else:
            cur.close()
            return datos

    def buscar_equipos(self, num):
        cur = self.cnn.cursor()
        sql = "SELECT * FROM equipos WHERE cod_equipo='{}' ".format(num)
        cur.execute(sql)
        datos = cur.fetchone()
        if datos == None:
            cur.close()
            return None
        else:
            cur.close()
            return datos

    def insertar_equipos(self, num, name,cant,est):
        cur = self.cnn.cursor()
        datos = self.buscar_equipos(num)
        if datos == None:
            sql = "INSERT INTO equipos (cod_equipo,nom_equipo,cant_equipo,estado) VALUES('{}','{}','{}','{}')".format(num,name,cant,est)
            cur.execute(sql)
            n= cur.rowcount
            self.cnn.commit()
            cur.close()
            return True
        else:
            return False
    
    def modifica_equipos(self,num, name,cap,est):
        datos = self.buscar_equipos(num)
        if datos != None:
            cur = self.cnn.cursor()
            sql='''UPDATE equipos SET  nom_equipo='{}', cant_equipo='{}', estado='{}' WHERE cod_equipo='{}' '''.format(name, cap, est,num)
            cur.execute(sql)
            n=cur.rowcount
            self.cnn.commit()    
            cur.close()
            return True
        else:
            return False

    def eliminar_equipos(self,num):
        datos = self.buscar_equipos(num)
        if datos != None:
            cur = self.cnn.cursor()
            sql = "DELETE FROM equipos WHERE cod_equipo = '{}'".format(num)
            cur.execute(sql)
            n=cur.rowcount
            self.cnn.commit()
            cur.close()
            return True
        else:
            return False 