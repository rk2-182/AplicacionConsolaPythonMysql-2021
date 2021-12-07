#Clase modelo la cual interactua con la BD (insertando,actualizando,etc)
import datetime
import mysql.connector
import hashlib

database = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="root",
    database="escuela",
    #port="3306"

)
#print(database)
cursor = database.cursor(buffered=True)

class Usuario:

    def __init__(self,nombre,apellidos,email,password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    
    def registrarUsuario(self):
        fecha = datetime.datetime.now()
        
        cifrar = hashlib.sha256()
        cifrar.update(self.password.encode('utf-8')) #codificar a bytes


        sql = "insert into usuarios values (null,%s,%s,%s,%s,%s)"
        usuario = (self.nombre,self.apellidos,self.email,cifrar.hexdigest(),fecha)

        try:

            #Ejecutar codigo sql y remplazar los datos
            cursor.execute(sql,usuario)
            #confirmar cambios
            database.commit()
        except:
            print('error, email ya registrado.')
        return [cursor.rowcount]


    def identificarUsuario(self):
        pass