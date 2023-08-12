class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangulo:
    def __init__(self, esquina_sup_izq, esquina_inf_der):
        self.esquina_sup_izq = esquina_sup_izq
        self.esquina_inf_der = esquina_inf_der

    def calcular_perimetro(self):
        base = abs(self.esquina_sup_izq.x - self.esquina_inf_der.x)
        altura = abs(self.esquina_sup_izq.y - self.esquina_inf_der.y)
        perimetro = 2 * (base + altura)
        return perimetro

    def calcular_area(self):
        base = abs(self.esquina_sup_izq.x - self.esquina_inf_der.x)
        altura = abs(self.esquina_sup_izq.y - self.esquina_inf_der.y)
        area = base * altura
        return area

    def es_cuadrado(self):
        base = abs(self.esquina_sup_izq.x - self.esquina_inf_der.x)
        altura = abs(self.esquina_sup_izq.y - self.esquina_inf_der.y)
        return base == altura

# Crear dos puntos para las esquinas del rectángulo
esquina_sup_izq = Punto(1, 5)
esquina_inf_der = Punto(7, 2)

# Crear una instancia de la clase Rectangulo
rectangulo1 = Rectangulo(esquina_sup_izq, esquina_inf_der)

# Calcular y mostrar el perímetro y el área del rectángulo
perimetro = rectangulo1.calcular_perimetro()
area = rectangulo1.calcular_area()
print("Perímetro del rectángulo:", perimetro)
print("Área del rectángulo:", area)

# Verificar si el rectángulo es un cuadrado
if rectangulo1.es_cuadrado():
    print("El rectángulo es un cuadrado.")
else:
    print("El rectángulo no es un cuadrado.")
