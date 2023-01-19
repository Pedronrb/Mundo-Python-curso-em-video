nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5 :
    print('O aluno ficou com a média {} e foi Reprovado'.format(media))
elif media > 5 and media < 7:
    print('O alunoficou com média {} e ficou de Recuperação'.format(media))
elif media >= 7:
    print('O aluno ficou com média {} e foi Aprovado'.format(media))