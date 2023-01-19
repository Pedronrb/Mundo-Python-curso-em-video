from datetime import date
atual = date.today().year
nasci = int(input('Ano de nascimento: '))
idade = atual - nasci
print('Quem nasceu em {} tem {} anos em {}'.format(nasci, idade, atual))
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade 
    print('Aindam falta {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter si alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
