valor = 0

def somaimposto(taxaimposto, custo):
    try:
        num1 = float(taxaimposto)
        num2 = float(custo)
    except:
        print('Digite um valor válido')
    
    valor = ((num1/100) * num2) + num2
    return valor


num1 = input('Digite a taxa do imposto em porcento: ')
num2 = input('Digite o custo do produto: ')

resultado = somaimposto(num1, num2)

print(f'O valor do produto com o imposto é: {resultado}')