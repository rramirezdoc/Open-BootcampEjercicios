from functools import reduce

def funcion(numeros):
    impares = filter(lambda x: x % 2 != 0, numeros)
    sumafinal = reduce(lambda x,y: x + y,impares)

    return sumafinal

print(funcion(range(500)))