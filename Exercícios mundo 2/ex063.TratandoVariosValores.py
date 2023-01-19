n = 0
count = 0
soma = 0
while n != 999:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    soma += n
    count += 1
print('Fim')
print(f'A soma é: {soma} e foram {count} vezes')