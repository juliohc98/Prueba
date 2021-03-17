import pymysql

db = pymysql.connect("127.0.0.1","prueba","prueba","test")
cursor = db.cursor()
# ejecuta el SQL query usando el metodo execute().

        # consulta de la tabla completa
cursor.execute("SELECT * FROM usuario")
data = cursor.fetchall()
for row in data:
    id = row[0]
    nombre = row[1]
    apellido = row[2]
    email = row[3]
    telefono = row[4]
    print ("id = {0}, nombre = {1}, apellido = {2}, email = {3}, telefono = {4}".format(id, nombre, apellido, email, telefono))

# desconecta del servidor
db.close()