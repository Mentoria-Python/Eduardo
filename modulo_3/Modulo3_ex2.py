premio = 45000

aposta_1 = 20
aposta_2 = 30
aposta_3 = 50

soma_aposta = aposta_1+ aposta_2 + aposta_3

print(f'A soma das apostas foram de :{soma_aposta} reais, e o prêmio é de :{premio}')

porcentagem_1 = (aposta_1 / soma_aposta) 
porcentagem_2 = (aposta_2 / soma_aposta) 
porcentagem_3 = (aposta_3 / soma_aposta) 

premio_1 = porcentagem_1 * premio 
premio_2 = porcentagem_2 * premio 
premio_3 = porcentagem_3 * premio 

print(f'Caso ganhe o apostador 1:{premio_1:.2f}, apostador 2: {premio_2:.2f}, apostador 3: {premio_3:.2f}')


