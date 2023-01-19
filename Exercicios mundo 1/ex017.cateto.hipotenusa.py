'''cat1 = float(input('Comprimento do cateto oposto: '))
cat2 = float(input('Comprimento do cateto adjacente: '))
hip = (cat1 ** 2 + cat2 **2) ** (1/2)
print(f'O valor da hipotenusa é: {hip:.2f}')'''

import math
cat1 = float(input('Comprimento do cateto oposto: '))
cat2 = float(input('Comprimento do cateto adjacente: '))
hip = math.hypot(cat1, cat2)
print(f'O valor da hipotenusa é: {hip:.2f}')