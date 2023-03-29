# Faça uma função que receba um objeto date, um valor inteiro "meses" 
# e retorne a data somando o valor em meses 

from datetime import datetime, date, timedelta

def diferenca(data, meses):
    data_1 = datetime.strptime(data, '%d-%m-%Y')
    meses_conv = timedelta(days=30*meses)
    resultado = data_1 + meses_conv
    return resultado

data = input('Digite a primeira data separando por "-": ').strip()
meses = input('Digite mêses a mais:": ').strip()
meses = int(meses)

resposta = diferenca(data, meses)
print(resposta)