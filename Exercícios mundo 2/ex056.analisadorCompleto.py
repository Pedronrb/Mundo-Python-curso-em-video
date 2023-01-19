somaIdade = 0
maiorIdade = 0
nomeVelho = ''
totMulher20 = 0
for p in range(1,6):
    print('----- {}° PESSOA -----'.format(p))
    nome = input('Nome? '.format(p))

    idade = int(input('Idade? '))
    
    sexo = input('[M/F]: ').strip()

    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdade = idade 
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdade:
        maiorIdade = idade
        nomeVelho = nome 
    if sexo in 'Ff' and idade < 20:
        totMulher20 += 1

print('A média de idade {}'.format(somaIdade/4))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdade, nomeVelho))
print('Ao todo são {} mulheres com 20 anos'.format(totMulher20))


