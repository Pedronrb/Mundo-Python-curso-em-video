numeros = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print(f'{n} foi inserido com sucesso...')
    else:
        print(f'O número {n} é repetido.')
    r = str(input('Quer continuar? S/N '))
    if r in 'Nn':
        break       
print('-=-'*30)
numeros.sort()
print(f'Você adicionou os valores {numeros}')
