# Declaracion de variables
puntuaciones = [100, 1, 50, 20]

# Creacion de un menu interactivo
def menu():
    print("Para cargar una puntuacion ingrese 1")
    print("Para saber la puntuacion mas alta ingrese 2")
    print("Para saber al ultima puntuacion agregada ingrese 3")
    print("Para saber las 3 puntuaciones mas altas ingrese 4")
    print("Para salir ingrese 5")
    n = int(input("Ingrese su opcion: "))
    if n == 1:
        ingresar_puntuacion()
    elif n == 2:
        puntuacion_mas_alta()
    elif n == 3:
        ultima_puntuacion()
    elif n == 4:
        top_players()
    elif n == 5:
        print("Adios")
    else:
        print("Ingrese un valor correcto")

# Funcion para ingresar puntuacion
def ingresar_puntuacion():
    global puntuaciones
    puntuacion = int(input("Ingrese su puntuacion: "))
    puntuaciones.append(puntuacion)
    menu()

# Funcion para buscar puntuacion mas alta
def puntuacion_mas_alta():
    global puntuaciones
    max_item = max(puntuaciones)
    print("puntuacion mas alta: ", max_item)
    menu()

# Funcion para buscar la ultima puntuacion
def ultima_puntuacion():
    global puntuaciones
    ultima = puntuaciones[-1]
    print("ultima puntuacion agregada: ", ultima)
    menu()

# Funcion para buscar las 3 puntuaciones mas altas
def top_players():
    global puntuaciones
    top = sorted(puntuaciones, reverse=True)[:3]
    print("Las 3 puntuaciones mas altas son: ", top)
    menu()

menu()



