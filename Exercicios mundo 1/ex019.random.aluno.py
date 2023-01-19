from random import choice 
al1 = str(input('Primeiro aluno? '))
al2 = str(input('Primeiro aluno? '))
al3 = str(input('terceiro aluno? '))
al4 = str(input('Quarto aluno? '))
lista = [al1, al2, al3, al4]
escolhido = choice(lista)
print(f'O aluno escolhido foi: {escolhido}')