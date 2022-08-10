numero_inicial = input('Ingrese numero inicial : ')
numero_final = input('Ingrese numero final : ')

numero_inicial = int(numero_inicial)
numero_final = int(numero_final)

while (numero_inicial <= numero_final):
    if (numero_inicial % 2):
        print(numero_inicial)
    numero_inicial += 1