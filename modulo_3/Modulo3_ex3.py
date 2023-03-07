segundos = input('Digite os segundos e saiba os minutos e horas: ')
segundos = int(segundos)

minutos = segundos  / 60
minutos_resto = segundos // 60
segundos_resto = segundos % 60

horas = minutos_resto / 60
horas_resto = minutos_resto // 60
minutos_hora_resto = minutos_resto % 60

print(f'São:{minutos_resto} minutos e {segundos_resto} segundos')
print(f'São:{horas_resto:.0f} horas, {minutos_hora_resto:.0f} minutos e {segundos_resto:.0f} segundos')
