import math
ângulo = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(ângulo))
cos = math.cos(math.radians(ângulo))
tg = math.tan(math.radians(ângulo))
print(f'O ângulo {ângulo}\nSENO: {seno:.2f}\nCOS: {cos:.2f}\nTAN: {tg:.2f}')