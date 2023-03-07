horas = input('Digite a hora atual: ')
minutos = input('Digite o minuto atual: ')
segundos = input('Digite o segundo atual: ')

tempo_duracao = input('Insira o tempo de duracao em segundos: ')

horas = int(horas)
minutos = int(minutos)
segundos = int(segundos)
tempo_duracao = int(tempo_duracao)

minutos_tempo_duracao = tempo_duracao // 60
segundos_tempo_duracao = tempo_duracao % 60

horas_tempo_duracao = minutos_tempo_duracao // 60
minutos_resto_tempo_duracao = minutos_tempo_duracao % 60

hora_certa = horas + horas_tempo_duracao
minuto_certo = minutos + minutos_resto_tempo_duracao
segundo_certo = segundos + segundos_tempo_duracao

print(f'A horário de início é - {horas}:{minutos}:{segundos}')
print(f'O horário de fim é - {hora_certa}:{minuto_certo}:{segundo_certo}')

