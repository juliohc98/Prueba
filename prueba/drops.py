# Se declara una variable que sea global para poder usarla mas adelante
numero = None

# Se crea una funcion que se llame asi misma para aseguararse de que el usuario ingrese un numero correcto 
def pedir_numero():
    global numero
    numero = int(input("Ingrese un numero: "))
    if numero <= 1:
        print("Ingrese un numero valido")
        pedir_numero()  
# Se llama a la funcion y se declara una lista vacia para rellenar en la siguiente funcion
pedir_numero()
primos = []

# Funcion que se encarga de comprobar si el numero es divisible entre 3,5 o 7
# almacenar cuantas veces, y en caso contrario almacenar el numero que no lo sea
def descomponer(n):

    global primos
    factores = [3, 5, 7]
    for i in factores:
        while n % i == 0:
            primos.append(i)
            n = n / i
        if i == 7:
            if n != 1:
                primos.append(n)
            break
    return primos

# Funcion que se encarga de recorrer la lista primos y escribir en pantalla el sonido correspondiente al mismo, o en dado caso el numero
def gotas(n):

    for i in n:
        if i == 3:
            print("Plic")
        elif i == 5:
            print("Plac")
        elif i == 7:
            print("Ploc")
        else:
            print(i)

# llamado a las funciones correspondientes
descomponer(numero)
gotas(primos)

