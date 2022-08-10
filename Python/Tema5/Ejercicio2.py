def numeroprimo(num):
    if num > 1:
        for i in range(2,int(num)):
            if (int(num) % i) == 0:
                return (f"El número {num} NO ES PRIMO")
                break
    else:
        return (f"El número {num} NO ES PRIMO")

    return (f"El número {num} ES PRIMO")

numero = int(input('Introduce un número entero: '))
print(numeroprimo(numero))