salario = float(input('Digite seu salário: R$'))
if salario <= 1250:
    salf = salario + (salario * 15 / 100)
    print('Seu salário com o aumento foi de R${:.2f}'.format(salf))
else:
    cal2 = salario * (15/100)
    salf2 = salario + (salario * 10 / 100)
    print('Seu salário com o aumento foi de R${:.2f}'.format(salf2))
