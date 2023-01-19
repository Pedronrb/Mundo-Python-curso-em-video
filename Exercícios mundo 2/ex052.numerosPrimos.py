numero = int(input('Digite um número: '))
total = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        print('\033[33m', end='') #se for divisível
        total += 1
    else:
        print('\033[34m', end='')
    print('{} '.format(i), end='')
print('\nO número {} foi divisível {} vezes'.format(numero, total))
if total == 2:
    print('É por isso que é primo')
else:
    print('É por isso que NÃO é primo')