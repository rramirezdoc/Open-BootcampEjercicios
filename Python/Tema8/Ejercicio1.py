nombreArchivo = str(input('Ingrese nombre de archivo : '))
nombreArchivo = nombreArchivo + '.txt'

linea1 = str(input('Ingrese primera linea : '))
f = open(nombreArchivo, 'x')
f.write(linea1 + '\n')
f.close()

linea2 = str(input('Ingrese segunda linea : '))
f = open(nombreArchivo, 'a')
f.write(linea2)
f.close()

datos = open(nombreArchivo, 'r').read()
print('Los datos del archivo son los siguientes : ')
print(datos)