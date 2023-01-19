num = int(input('Digite um número: '))
if num % 2 == 0:
    print('O número {} é par'.format(num))
else:
    if num % 1 == 0 or num % num == 0:
        print('O número {} é ímpar'.format(num))