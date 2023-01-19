from random import randint
from time import sleep
print('-=-' * 20)
jogador = int(input('Pense em um número de 0 a 5: ')) #jogador tenta advivinhar
print('PROCESSANDO...')
sleep(1)
computador = randint(0, 5) #sortea o número
print('-=-' * 20)
if (jogador == computador):
    print('Parabéns!! Ganhou da máquina.')
else:
    print('Não acertou, pois a máquina colocou {} e você {}'.format(computador, jogador))
