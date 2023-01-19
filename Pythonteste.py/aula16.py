lanche = ('Hambúrger', 'suco', 'pizza', 'pudim') #Pode ser com ou sem parenteses
#() >> Tupla / [] >> Lista / {} >> Dicionário
print(lanche[1])
print(lanche[-3:])

#TUPLAS SÃO IMUTÁVEIS
#lanche[1] = 'refrigerante'

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for c in lanche:
    print(f'Eu irei comer {c}')
print('Comi bastante')
