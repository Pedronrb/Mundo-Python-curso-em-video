ValorCasa = float(input('Digite o valor da casa: R$'))
Salario = float(input('Quanto você ganha? ' ))
Anos = float(input('Quantos anos quer pagar? '))
Prestação = ValorCasa / (Anos * 12)
minimo = Salario * 30/100 

if Prestação <= minimo:
    print('Empréstimo pode ser CONCEDIDO ')
else:
    print('Empréstimo NEGADO!!')
print('Para pagar uma casa de R${:.2f} em {:.0f} anos, a prestação ficará por R${:.2f}'.format(ValorCasa, Anos, Prestação))
