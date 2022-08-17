import Operaciones as op

num1 = int(input('Ingrese primer numero : '))
num2 = int(input('Ingrese segundo numero : '))

opera = input('Seleccione operacion (1:suma - 2:resta - 3:multiplicacion - 4:division) : ')

match opera:
    case "1":
        print('El resultado es : ' + str(op.suma(num1, num2)))

    case "2":
        print('El resultado es : ' + str(op.resta(num1, num2)))

    case "3":
        print('El resultado es : ' + str(op.multiplica(num1, num2)))
    
    case "4":
        print('El resultado es : ' + str(op.divide(num1, num2)))

    case _:
        print("No existe la operacion.")