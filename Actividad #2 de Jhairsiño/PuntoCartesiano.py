import math


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar(self):
        print("Su punto se ha transladado a:", self.x, ",", self.y)

    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y
        print("Su punto se ha transladado a:", self.x, ",", self.y)

    def calcular_distancia(self, otro_punto):
        distancia = math.sqrt((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2)
        return distancia


# Crear una instancia de la clase Punto
punto1 = Punto(3, 4)

# Mostrar el punto
punto1.mostrar()

# Mover el punto a nuevas coordenadas
punto1.mover(7, 9)

# Mostrar el punto nuevamente después de moverlo
punto1.mostrar()

# Crear otro punto
punto2 = Punto(1, 2)

# Calcular la distancia entre los dos puntos
distancia = punto1.calcular_distancia(punto2)
print("Distancia entre los dos puntos:", distancia)
