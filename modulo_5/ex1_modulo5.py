# Faça uma função que receba duas datas 
# e retoirne a diferença em dias entre elas.

from datetime import datetime

def diferenca(data_1, data_2):
    resultado_1 = datetime.strptime(data_1, '%d-%m-%Y')
    resultado_2 = datetime.strptime(data_2, '%d-%m-%Y')
    resultado = resultado_1 - resultado_2
    return resultado

data_1 = input('Digite a primeira data separando por "-": ').strip()
data_2 = input('Digite a segunda data separando por "-": ').strip()

dias = diferenca(data_1, data_2)
print(f'a diferença é {dias} dias')