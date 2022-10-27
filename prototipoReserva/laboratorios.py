import mysql.connector

class Laboratorios:
    def __init__(self):
        #!!!!!!!!!!!!!!! importante cambiar la conexio a la base de datos
        self.cnn = mysql.connector.connect(host="localhost", user="root", passwd="guille",database="is2proyecto") # cambiar cada que se haga un pull
    
    def __str__(self):
        datos = self.consulta_laboratorios()
        aux = ""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux

    def consulta_laboratorios(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM laboratorio")
        datos = cur.fetchall()
        if len(datos) == 0:
            cur.close()
            return None
        else:
            cur.close()
            return datos

    def buscar_laboratorio(self, num):
        cur = self.cnn.cursor()
        sql = "SELECT * FROM laboratorio WHERE num_laboratorio='{}' ".format(num)
        cur.execute(sql)
        datos = cur.fetchone()
        if datos == None:
            cur.close()
            return None
        else:
            cur.close()
            return datos

    def insertar_laboratorios(self, num, name,cant):
        cur = self.cnn.cursor()
        datos = self.buscar_laboratorio(num)
        if datos == None:
            sql = "INSERT INTO laboratorio (num_laboratorio,tip_lab,capacidad) VALUES('{}','{}','{}')".format(num,name,cant)
            cur.execute(sql)
            n= cur.rowcount
            self.cnn.commit()
            cur.close()
            return True
        else:
            return False
    
    def modifica_laboratorio(self,num, name,cap):
        datos = self.buscar_laboratorio(num)
        if datos != None:
            cur = self.cnn.cursor()
            sql='''UPDATE laboratorio SET  tip_lab='{}', capacidad='{}' WHERE num_laboratorio='{}' '''.format(name, cap,num)
            cur.execute(sql)
            n=cur.rowcount
            self.cnn.commit()    
            cur.close()
            return True
        else:
            return False

    def eliminar_laboratorio(self,num):
        datos = self.buscar_laboratorio(num)
        if datos != None:
            cur = self.cnn.cursor()
            sql = "DELETE FROM laboratorio WHERE num_laboratorio = '{}'".format(num)
            cur.execute(sql)
            n=cur.rowcount
            self.cnn.commit()
            cur.close()
            return True
        else:
            return False 