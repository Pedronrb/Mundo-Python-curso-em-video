resp = 'S'
soma = 0
count = 0
menor = maior = 0

while resp in 'Ss':
    n = int(input('Digite o valor: '))
    count += 1
    soma += n

    if count == 1:
        maior = menor = n
    else:
        if n < menor:
            menor = n
        elif n > maior:
            maior = n
    resp = str(input('Quer continuar S/N ? ')).upper().strip()
media = soma / count
print(f'Voce digitou {count} números, a média foi {media}\nO maior foi {maior} e o menor {menor}')
