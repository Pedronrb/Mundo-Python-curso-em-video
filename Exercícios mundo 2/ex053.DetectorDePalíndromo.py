frase = str(input('Digite a frase: ')).strip().upper() #strip - remove os espaços / Upper - Maiúsculo
palavras = frase.split('A') # dividi a palavra em índices
junto = ''.join(palavras)
inverso = ''
for i in range(len(junto) - 1, -1, -1):
    inverso += junto[i]
if inverso == junto:
    print('Temos um palíndomo')
else:
    print('A frase digitada não é um palíndromo')

