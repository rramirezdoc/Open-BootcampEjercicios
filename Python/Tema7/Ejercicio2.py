import time as t

hora = t.strftime('%H')
minutos = t.strftime('%M')
segundos = t.strftime('%S')

print('Hora actual -> ' + hora + ':' + minutos + ':' + segundos)

if int(hora) < 19:
    print('Aun no es hora de ir a casa')
    print('Faltan ' + str(18 - int(hora)) + ' horas y ' + str(59 - int(minutos)) + ' minutos')
else:
    print('Ya puedes ir a casa')