nome = str(input('Qual é o seu nome? '))
if nome == 'Pedro':
    print('Você é foda:)')
elif nome == 'Maria' or nome == 'João' or nome == 'Júlia':
    print('Seu nome é bem popular')
elif nome in 'Larrisa Fernanda Camila':
    print('Belo nome feminino')
else:
    print('Tenha uma bom dia {}'.format(nome))