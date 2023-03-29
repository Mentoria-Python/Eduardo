# Faça uma função que receba valor em segundos,
# e retorne o horário no formato "00h00m00s"

def hora_formatar(segundos):

   horas = segundos // 3600
   minutos = (segundos % 3600) // 60
   segundos = segundos % 60
   lista = [horas, minutos, segundos]
   return lista


segundos = input('Digite os segundos e saiba os minutos e horas: ')
segundos = int(segundos)

formato = hora_formatar(segundos)

print(f'{formato[0]:02d}h{formato[1]:02d}m{formato[2]:02d}s')

