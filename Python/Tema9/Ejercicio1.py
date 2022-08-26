listapaises = input("Ingrese listado de paises (separados por comas) : ")

paises = listapaises.split(',')

print(",".join(sorted(paises)))