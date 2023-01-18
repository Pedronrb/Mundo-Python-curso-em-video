palavras = ('Pedro','Findout','Project','Life','Strog','Big','MASTER','BRUNCH','GOOD','SPECTRO','XUXA')
for p in palavras:
    print(f'\nTemos a palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra in 'AEIOUaeiou':
            print(letra.lower(), end=' ' )