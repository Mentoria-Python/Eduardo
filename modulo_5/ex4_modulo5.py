# Faça uma função que receba um objeto Date, um valor inteiro
# "dias" e retorne a data menos o valor em dias.

from datetime import datetime, date, timedelta

def diferenca(data, dias):
    data_1 = datetime.strptime(data, '%d-%m-%Y')
    dias_conv = timedelta(dias)
    resultado = data_1 - dias_conv
    return resultado

data = input('Digite a primeira data separando por "-": ').strip()
dias = input('Digite dias a menos:": ').strip()
dias = int(dias)

resposta = diferenca(data, dias)
print(resposta)