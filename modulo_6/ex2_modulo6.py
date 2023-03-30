# Faça um programa que leia três números inteiros, em seguida mostre o maior e o menor número deles

def teste_maior():
    
    lista = []
    for i in range(3):
        valor = input('Digite um número: ')
        lista.append(valor)
    lista.sort()

    print(f'O maior número é {lista[2]}, e o menor é {lista[0]}')

teste_maior()
