num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print('{} é maior que {}'.format(num1, num2))
elif num2 > num1:
    print('{} é maior que {}'.format(num2, num1))
else: 
    print('{} e {} são iguais'.format(num1, num2))