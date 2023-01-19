from random import randint

computador = randint(0,10)
print('Acabei de pensar entre um número entra 0 e 10')
print('Consegue adivinhar?') 
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Menos')
        elif jogador < computador:
            print('Mais')
print("Acertou em {} palpites".format(palpite))