#Faça um programa que verifique se uma letra digitada é vogal ou consoante

def teste_vogais(letra):
    
    vogais = ['a', 'e', 'i', 'o', 'u']
    
    for i in vogais:
        if i == letra:
            return f'A letra "{letra}" é vogal'
        else:
            return f'A letra "{letra}" é consoante'

valor = input('Digite a letra: ').lower().strip()

print(teste_vogais(valor))








