'''
Suporndo que a população de um país A seja da ordem de 80000 habitantes 
com uma taxa anual de crescimento de 3% e que a população de B seja 200000
habitates com uma taxa de cresimento de 1.5%. Faça um programa que calcule 
e escreva o número de anos necessários para que a população do país A ultrapasse ]
ou iguale a população do país B, mantidas as taxas de crescimento. 

'''
populacao_1 = 80000
populacao_2 = 200000

taxa_1 = 0.03
taxa_2 = 0.015
anos = 0

while populacao_1 < populacao_2:
    populacao_1 = (populacao_1) + (populacao_1 * taxa_1)    
    populacao_2 = (populacao_2) * (populacao_2 * taxa_2)
    anos += 1

print(anos)
