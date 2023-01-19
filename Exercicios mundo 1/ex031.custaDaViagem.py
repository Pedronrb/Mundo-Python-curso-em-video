num = float(input('Digite a distância da viagem: '))
if num <= 200:
    cal = num * (1/2)
    print('O valor da viagem foi R${:.2f} com a distância de {:.0f}km'.format(cal,num))
else:
    cal1 = num * (45/100)
    print('O valor da viagem foi R${:.2f} com a distância de {:.0f}km'.format(cal1, num))