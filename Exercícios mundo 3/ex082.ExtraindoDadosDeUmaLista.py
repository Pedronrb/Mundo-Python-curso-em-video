valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? S/N  '))

    if resp in 'SsNn':
        break
print('-=-' * 30)
print(f'Você digitou {len(valores)} elementos.')

valores.sort(reverse=True)
print(f'Os valores em ordem descrescente são {valores}')
if 5 in valores:
    print('O cinco está dentro dos valores')
else:
    print('O cinco NÃO está na lista')