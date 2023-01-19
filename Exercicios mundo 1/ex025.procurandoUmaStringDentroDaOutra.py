#Crie um programa q leia o nome de uma pessoa e diga se tem "Silva"
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva: {}'.format('SILVA' in nome.upper()))

