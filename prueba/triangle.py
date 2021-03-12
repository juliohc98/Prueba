# Importaciones necesarias
import math
from math import sqrt 

# Declaracion de variables
triangulo = None 

# Funcion para que el usuario ingrese un numero valido
def tipo_triangulo():
    global triangulo
    triangulo = int(input("Ingrese un numero: "))
    if triangulo < 1 or triangulo > 4:
        print("Ingrese un numero valido")
        tipo_triangulo() 

# Creacion de la clase principal Triangles
class Triangles:
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

# Creacion de subclases especificas para cada tipo de triangulo y su metodo para calcular el area
class equilatero(Triangles):
    def __init__(self, a,b,c):
        super().__init__(a,b,c)

    def area(self):
        h = (( 3*a ) ** 0.5 ) / 2
        area = (b*h) / 2
        return area

class isosceles(Triangles):
    def __init__(self, a,b,c):
        super().__init__(a,b,c)

    def area(self):
        h = (a**2-((b**2)/4)) ** 0.5
        area = (b*h) / 2
        return area

class escaleno(Triangles):
    def __init__(self, a,b,c):
        super().__init__(a,b,c)

    def area(self):
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        return area

class rectangulo(Triangles):
    def __init__(self, a,b,c):
        super().__init__(a,b,c)

    def area(self):
        area = (b*a) / 2
        return area
    
# Menu interactivo para el usuario
print("escoja su tipo de triangulo")
print("Para equilatero marque 1")
print("Para isosceles marque 2")
print("Para escaleno marque 3")
print("Para rectangulo marque 4")

# Llamado a la funcion y rellenar los valores de los lados del triangulo
tipo_triangulo()

print("ingrese los valores de los lados del triángulo")
a= int(input("a= "))
b= int(input("b= "))
c= int(input("c= "))

# Respuesta arrojada por el programa dependiendo de la opcion 
if triangulo == 1:
    t = equilatero(a,b,c)
    print("area de equilatero: {}".format(t.area()))
elif triangulo == 2:
    t2 = isosceles(a,b,c)
    print("area de isosceles: {}".format(t2.area()))
elif triangulo == 3:
    t3 = escaleno(a,b,c)
    print("area de escaleno: {}".format(t3.area()))
elif triangulo == 4:
    t4 = rectangulo(a,b,c)
    print("area de rectangulo: {}".format(t4.area()))
