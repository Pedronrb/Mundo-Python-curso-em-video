print('-=-'*20)
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: ')) 
r3 = float(input('Terceira fase: '))
print('-=-'*20)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podemo FORMAR triângulos')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')

