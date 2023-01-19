n = int(input('Qual a tabuada? '))
count = 0
print('-=-'*30)
print(f'Tabuada do valor: {n}')
while count <= 10: 
    multi = n * count
    print(f'{n} x {count} = {multi}')
    count += 1
    
print('-=-'*30)  