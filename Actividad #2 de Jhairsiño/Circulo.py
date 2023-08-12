import math


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        area = math.pi * self.radio ** 2
        return area

    def calcular_perimetro(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro

    def punto_pertenece(self, punto):
        distancia = math.sqrt((punto.x - self.centro.x) ** 2 + (punto.y - self.centro.y) ** 2)
        return distancia <= self.radio



punto_1 = Punto(3, 4)


circulo_1 = Circulo(Punto(2, 2), 5)

area = circulo_1.calcular_area()
print("Área:", area)


perimetro = circulo_1.calcular_perimetro()
print("Perímetro:", perimetro)


is_inside = circulo_1.punto_pertenece(punto_1)
if is_inside:
    print("El punto está dentro del círculo.")
else:
    print("El punto está fuera del círculo.")

