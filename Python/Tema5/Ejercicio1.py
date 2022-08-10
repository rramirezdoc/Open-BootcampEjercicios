import math

def areaTriangulo(base, altura):
    return (base*altura)/2

def areaCirculo(radio):
    return math.pi * (radio ** 2)

base = int(input('Ingrese base de triangulo : '))
altura = int(input('Ingrese altura de triangulo : '))
print('El área del triangulo es : ' + str(areaTriangulo(base,altura)))

radio = int(input('Ingrese radio del circulo : '))
print('El area del circulo es : ' + str(areaCirculo(radio)))