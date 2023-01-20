num = []
pares = []
impares = []
while True:
    num.append( int(input("Digite um valor: ")))
    resp = str(input(f'Quer continuar ? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=-' * 40)
print(f'A lista completa é {num}')
print(f'A lista de PARES é {pares}')
print(f'A lista de ÍMPARES é {impares}')
