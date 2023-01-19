soma = 0
pares = ''
for c in range(1,7):
    c = int(input(' Digite o {} valor: '.format(c)))
    if c % 2 == 0:
        pares += str(c) + '  '
        soma += c 
print('A soma é {} e os números são {}'.format(soma, pares))
    