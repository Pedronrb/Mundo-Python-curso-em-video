n1 = float(input('primeira nota?'))
n2 = float(input('Segunda nota ?'))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6:
    print('Sua nota está acima da média')
else:
    print('Nota abaixo da média')