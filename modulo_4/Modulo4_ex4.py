
pagamento = 0

def valorPagamento(prestacao, dias):

    if dias == 0:
        pagamento = prestacao
    else:
        pagamento = prestacao + ((0.03 * prestacao) + ((0.001 * prestacao)* dias))

    return pagamento

while True:

    valor_prestacao = input('Digite o valor da prestação: ')
    valorpre = float(valor_prestacao)
    dias_atrasado = input('Quantos dias está atrasado? ')
    diasatr = float(dias_atrasado)

    while valor_prestacao != 0:

        recebe = valorPagamento(valorpre, diasatr)
        print(f'O valor a ser pago é {recebe}')

        break
    break