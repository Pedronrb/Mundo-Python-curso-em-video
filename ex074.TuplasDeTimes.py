times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')
print('-=-'*15)
print(f'Lista dos times {times}')
print('-=-'*15)
print(f'Os primeiros 5 colocados são {times[0:5+1]}')
print('-=-'*15)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('-=-'*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O Chapecoense está na posição: {times.index("Chapecoense")}')