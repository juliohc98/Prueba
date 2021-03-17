import pymysql

db = pymysql.connect("127.0.0.1","prueba","prueba","test")
cursor = db.cursor()

        # insertar nuevo registro
sql = "INSERT INTO usuario(nombre, apellido, email, telefono) \
   VALUES ('{0}','{1}','{2}','{3}')".format("julio3","hidalgo3","juliohc98@gmail.com", "04241391995")
try:
   # ejecutar el comando
   cursor.execute(sql)
   print("agregado correctamente")
   # subir los cambios
   db.commit()
except:
   # en caso de error
   db.rollback()


# desconectar del servidor
db.close()