convertido = 0
hora = 0
minuto = 0


def conversao(hr, min):
    
    if hr >= 0 and hr <= 12 and min <=59:
        conv = 'A.M'
        A = hr
    elif hr > 12 and hr <= 24 and min <=59:
        conv = 'P.M'
        A = hr - 12
    else:
        print('Digite um horário válido')
    
    return A, min, conv


while True:

    var_escolha = input('Digite [i] para incluir ou [s] para sair:').lower().strip()

    if var_escolha == 'i':
        horas = input('Digite o inteiro da hora: ')
        minutos = input('Digite o minutos: ')
        hora = int(horas)
        minuto = int(minutos)

        tup_hr = conversao(hora, minuto)

        print(f'A hora é {tup_hr[0]}:{tup_hr[1]} {tup_hr[2]}')
    
    if var_escolha == 's':
        print("Você saiu do programa!!")
        break
    
    