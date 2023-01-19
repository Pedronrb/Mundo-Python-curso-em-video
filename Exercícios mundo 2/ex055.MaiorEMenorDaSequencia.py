list = []
peso = []
maiorPeso = 0
menorPeso = 0
for i in range(1, 3):
    pessoas = str(input('Nome da {}° pessoa? '.format(i)))
    kg = float(input('Qual o peso da {}° pessoa? '.format(i)))
    list.append(pessoas)
    peso.append(kg)
for i in range(len[peso] - 1):

    if peso[i] > peso[i+1]:
        maiorPeso = peso[i]
        menorPeso = peso[i+1]
    else:
        menorPeso = peso[i]

print(list)