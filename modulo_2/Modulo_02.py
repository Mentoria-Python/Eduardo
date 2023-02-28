lista =['a A4-Verde-Comercial Trifásica 220/127','b A4-Verde-Rural Bifásica 380/220','c B3-Industrial Monofásica 220']

posi1 = lista[0].split()
posi2 = lista[1].split()
posi3 = lista[2].split()

valor = input('Digite a, b ou c: ')

if valor == 'a':
    print(posi1[0] + ' - ' + posi1[2] + ' ' + posi1[3])
elif valor == 'b':
    print(posi2[0] + ' - ' + posi2[2] + ' ' + posi2[3])
elif valor == 'c':
    print(posi3[0] + ' - ' + posi3[2] + ' ' + posi3[3])