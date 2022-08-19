from pickle import *

class Vehiculo:
    color = ''
    puertas = 0

    def __init__(self, color, puertas) -> None:
        self.color = color
        self.puertas = puertas

    def __str__(self) -> str:
        return 'Color : ' + self.color + ' - Puertas : ' + str(self.puertas)

auto1 = Vehiculo('blanco', 4)
print(auto1)

f = open('auto.txt', 'w+b')
dump(auto1, f)

f.seek(0)
nuevo_auto = load(f)

print(nuevo_auto)

f.close()