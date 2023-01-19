from datetime import date
list = []
menor = 0
maior = 0

for i in range(1,8,1):
    ano = int(input('Digite o ano de nascimento da {}° pessoa: '.format(i)))
    list.append(ano)
for i in range(len(list)):
    if (date.today().year - list[i]) >= 18:
        maior += 1
    else:
        menor += 1
print('Tem {} maiores e {} menores'.format(maior, menor))