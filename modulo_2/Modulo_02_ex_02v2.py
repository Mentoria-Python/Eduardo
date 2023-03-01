a = 'A4-Verde-Comercial Trifásica 220/127'
b = 'A4-Verde-Rural Bifásica 380/220'
c = 'B3-Industrial Monofásica 220'

posicao_a = a.find(" ")
posicao_b = b.find(" ")
posicao_c = c.find(" ")

conexao_a = a[posicao_a:]
conexao_b = b[posicao_b:]
conexao_c = c[posicao_c:]

print('a -{}\nb -{}\nc -{}'.format(conexao_a, conexao_b, conexao_c))