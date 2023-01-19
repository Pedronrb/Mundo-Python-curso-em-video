print(20*"=")
print('CADASTRE UMA PESSOA')
print(20*"=")

tot18 = 0
totM = 0
totF = 0

while True:

    idade = int(input('Idade: '))
    sexo = ' '

    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    if idade >= 18:
        tot18 += 1

    if sexo == 'M':
        totM += 1

    if sexo == 'F' and idade < 20:
        totF += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break   

print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Total de homens é : {totM}')
print(f'Total de mulheres com menos de 20 abos é: {totF}')
 

print(20*"=")