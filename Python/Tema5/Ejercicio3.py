def añobisiesto(num):
  if(num % 4 == 0 and (num % 100 != 0 or num % 400 == 0)):
      return (f"El año {num} es bisiesto")
  else:
      return (f"El año {num} NO es bisiesto")

año = int(input('Introduce un año: '))
print(añobisiesto(año))
