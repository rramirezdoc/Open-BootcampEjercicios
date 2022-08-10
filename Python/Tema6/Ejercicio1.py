class Vehiculo:
    color = None
    ruedas = 0
    puertas = 0

class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 0

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Velocidad {self.velocidad} - Cilindrada {self.cilindrada} - Color {self.color} - Ruedas {self.ruedas} - Puertas {self.puertas} "

coche = Coche("Gris", 4, 5, 200, 1600)
print(coche)    