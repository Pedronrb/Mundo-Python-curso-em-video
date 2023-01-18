from random import randint

v = 0

while True:
    jogador = int(input('Diga uma valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('Par ou Ímpar? [P/I]').strip().upper()
    print(f'você jogou {jogador} e o computador jogou {computador} e o total foi {total}')
    print(f'DEU PAR !!' if total % 2 == 0 else 'DEU Ímpar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!!')
            v += 1
        else:
            print('Você PERDEU!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!!')
            v += 1 
        else:
            print('VoccÊ PERDEU!!')
            break
    print('Vamos jogar novamente...')
print(f'GAMER OVER!! Você VENCEU {v} vezes.')
