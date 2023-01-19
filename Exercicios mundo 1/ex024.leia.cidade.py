cid = str(input('Digite a sua cidade: '))
quebra = cid.split()

if quebra[0] == 'Santo' or quebra[0] == 'santo':
    print(f'Sua cidade é : {cid}')
else:
    print('Sua cidade não começa com Santo')


