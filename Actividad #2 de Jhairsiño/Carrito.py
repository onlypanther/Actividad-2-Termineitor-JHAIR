
class Vehículo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje


vehiculo1 = Vehículo(200, 15000)


print("Velocidad máxima:", vehiculo1.velocidad_maxima)
print("Kilometraje:", vehiculo1.kilometraje)
