import mysql.connector

class Materiales:
    def __init__(self):
        #!!!!!!!!!!!!!!! importante cambiar la conexio a la base de datos
        self.cnn = mysql.connector.connect(host="localhost", user="root", passwd="samuel",database="is2proyecto") # cambiar cada que se haga un pull
    
    def __str__(self):
        datos = self.consulta_materiales()
        aux = ""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux

    def consulta_materiales(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM materiales")
        datos = cur.fetchall()
        if len(datos) == 0:
            cur.close()
            return None
        else:
            cur.close()
            return datos

    def buscar_materiales(self, num):
        cur = self.cnn.cursor()
        sql = "SELECT * FROM materiales WHERE cod_material='{}' ".format(num)
        cur.execute(sql)
        datos = cur.fetchone()
        if datos == None:
            cur.close()
            return None
        else:
            cur.close()
            return datos

    def insertar_materiales(self, num, name,cant):
        cur = self.cnn.cursor()
        datos = self.buscar_materiales(num)
        if datos == None:
            sql = "INSERT INTO materiales (cod_material,nom_material,cant_material) VALUES('{}','{}','{}')".format(num,name,cant)
            cur.execute(sql)
            n= cur.rowcount
            self.cnn.commit()
            cur.close()
            return True
        else:
            return False
    
    def modifica_materiales(self,num, name,cap):
        datos = self.buscar_materiales(num)
        if datos != None:
            cur = self.cnn.cursor()
            sql='''UPDATE materiales SET  nom_material='{}', cant_material='{}' WHERE cod_material='{}' '''.format(name, cap,num)
            cur.execute(sql)
            n=cur.rowcount
            self.cnn.commit()    
            cur.close()
            return True
        else:
            return False

    def eliminar_materiales(self,num):
        datos = self.buscar_materiales(num)
        if datos != None:
            cur = self.cnn.cursor()
            sql = "DELETE FROM materiales WHERE cod_material = '{}'".format(num)
            cur.execute(sql)
            n=cur.rowcount
            self.cnn.commit()
            cur.close()
            return True
        else:
            return False 