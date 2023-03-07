consumo_anual = input('Digite o seu consumo anual: ')
geracao_energia = input('Digite a geracao de energia: ')

consumo_anual = float(consumo_anual)
geracao_energia = float(geracao_energia)

porcentagem = (geracao_energia / consumo_anual) * 100

print(f'A sua instalação solar cobre {porcentagem:.2f} % do seu consumo')
