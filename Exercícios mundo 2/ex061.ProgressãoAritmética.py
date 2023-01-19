primeiro = int(input('Primeiro termo? '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -- ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input("Quantos termos vocÊ quer mostrar mais? "))
print(f'Progressão finalizada com {total} termos mostrado.')