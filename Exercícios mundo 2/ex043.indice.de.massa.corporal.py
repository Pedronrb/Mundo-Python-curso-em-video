peso = float(input('Digite seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é {:.2f} e você está ABAIXO DO PESO'.format(imc))
elif imc > 18.5 and imc < 25:
    print('Seu IMC é {:.2f} e você está no PESO IDEAL'.format(imc))
elif imc > 25 and imc < 30:
    print('Seu IMC é {:.2f} e você está SOBREPESO'.format(imc))
elif imc > 30 and imc < 40:
    print('Seu IMC é {:.2f} e você está com OBESIDADE'.format(imc))
else:
    print('Seu IMC é {:.2f} e você está com OBESIDADE MÓRBIDA'.format(imc))