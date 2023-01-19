dias = int(input('Quantidade de dias? '))
kmt = float(input('Quantidade de km percorrido? '))

pagarPorKm = kmt * 0.15
pagarPorDias = dias * 60
print(f'Valor a pagar por Km foi: R${pagarPorKm:.2f}\nO valor a pagar por dias: R${pagarPorDias:.2f}')
print(f'Total: R${pagarPorDias + pagarPorKm:.2f}')