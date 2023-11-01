class TransporteUrbano:
    def __init__(self, tipo, marca, modelo):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo

    def obtener_informacion(self):
        return f'Tipo: {self.tipo}, Marca: {self.marca}, Modelo: {self.modelo}'


class Automovil(TransporteUrbano):
    def __init__(self, marca, modelo):
        super().__init__("Automóvil", marca, modelo)


class Bicicleta(TransporteUrbano):
    def __init__(self, marca, modelo):
        super().__init__("Bicicleta", marca, modelo)


class Scooter(TransporteUrbano):
    def __init__(self, marca, modelo):
        super().__init__("Scooter", marca, modelo)


# Ejemplo de uso
if __name__ == "__main__":
    automovil1 = Automovil("Toyota", "Corolla")
    bicicleta1 = Bicicleta("Trek", "Mountain Bike")
    scooter1 = Scooter("Xiaomi", "Mi Electric Scooter")

    print("\n",automovil1.obtener_informacion())
    print(bicicleta1.obtener_informacion())
    print(scooter1.obtener_informacion(),"\n")