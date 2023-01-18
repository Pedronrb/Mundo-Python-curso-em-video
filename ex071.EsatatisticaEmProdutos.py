total = totMil = menor = cont = 0
while True:
    produto  = str(input('Nome do produto: '))
    preco = float(input('Valor do produto R$ '))
    cont += 1
    total += preco
    
    if preco > 100:
        totMil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S//N] ')).strip().upper()[0]
    if resp == 'N':
        break    
    
print('Fim do programa')
print(f'O total de compras foi R${total:.2f}')
print(f'Temos {totMil} produtos que custa mais R$1000.00')
print(f'P produto mais barato foi {barato} e custa R${menor:.2f}')