cont = soma = 0

while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Você digitou {cont} e a soma dos números é: {soma}')
