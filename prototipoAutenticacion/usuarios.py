import mysql.connector

class Usuarios:
    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", passwd="samuel",database="is2proyecto")
    
    def __str__(self):
        datos = self.consulta_usuarios()
        aux = ""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux

    def consulta_usuarios(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM usuarios")
        datos = cur.fetchall()
        if len(datos) == 0:
            cur.close()
            return None
        else:
            cur.close()
            return datos

    def buscar_usuario(self, usr):
        cur = self.cnn.cursor()
        sql = "SELECT user,cast(aes_decrypt(password, '123') as char) FROM usuarios WHERE user='{}' ".format(usr)
        cur.execute(sql)
        datos = cur.fetchone()
        if datos == None:
            cur.close()
            return None
        else:
            cur.close()
            return datos

    def insertar_usuario(self, usr, password):
        cur = self.cnn.cursor()
        datos = self.buscar_usuario(usr)
        if datos == None:
            sql = "INSERT INTO usuarios (user,password) VALUES('{}',aes_encrypt('{}','123'))".format(usr,password)
            cur.execute(sql)
            n= cur.rowcount
            self.cnn.commit()
            cur.close()
            return True
        else:
            return False
