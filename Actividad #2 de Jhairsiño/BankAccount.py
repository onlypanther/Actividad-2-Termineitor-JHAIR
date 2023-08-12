class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
            print("Depósito completado. Su saldo ahora es:", self.balance)
        else:
            print("La cantidad a depositar debe ser mayor que cero.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.balance:
            self.balance -= cantidad
            print("Retiro completado. Su saldo ahora es:", self.balance)
        else:
            print("No tienes suficientes fondos o la cantidad no es válida.")

    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        print("Cuota de manejo aplicada. Su saldo ahora es:", self.balance)

    def mostrar_detalles(self):
        print("Número de cuenta:", self.numero_cuenta)
        print("Propietarios:", self.propietarios)
        print("Saldo:", self.balance)


# Crear una instancia de la clase CuentaBancaria
cuenta1 = CuentaBancaria("123456", ["Jhairsiño el mascapito"], 1000)

# Realizar operaciones en la cuenta
cuenta1.depositar(500)
cuenta1.retirar(200)
cuenta1.aplicar_cuota_manejo()

# Mostrar detalles de la cuenta
cuenta1.mostrar_detalles()

