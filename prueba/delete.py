import pymysql

db = pymysql.connect("127.0.0.1","prueba","prueba","test")
cursor = db.cursor()

        # insertar nuevo registro
sql = "DELETE FROM usuario WHERE id = {}".format("9")
try:
   # ejecutar el comando
   cursor.execute(sql)
   print("borrado correctamente")
   # subir los cambios
   db.commit()
except:
   # en caso de error
   db.rollback()


# desconectar del servidor
db.close()