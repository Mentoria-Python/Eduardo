# Faça uma função que recebe duas datas
# e retorne a difereça em horas entre eles.

from datetime import datetime, timedelta

def diferenca(data_1, data_2):
    resultado_1 = datetime.strptime(data_1, '%d-%m-%Y %H:%M:%S')
    resultado_2 = datetime.strptime(data_2, '%d-%m-%Y %H:%M:%S')
    resultado = resultado_1 - resultado_2
    return resultado

data_1 = input('Digite a primeira data separando por "-" e a hora por ":": ').strip()
data_2 = input('Digite a segunda data separando por "-" e a hora por ":": ').strip()

dias = diferenca(data_1, data_2)

horas = int(dias.total_seconds()/3600)
print(f'a diferença é {horas} horas')