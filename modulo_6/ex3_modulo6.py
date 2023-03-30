# Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido
# e continue pedindo até que o usuário informe um valor válido.

def pede_nota():
    
    while True:
        nota = input('Digite a nota: ')
        nota = int(nota)
        
        if nota > 0 and nota < 10:
            return f'a nota é :{nota}'
        else:
            print('nota não válida')
            continue
 
var = pede_nota()

print(var)