velo = float(input('Digite a velocidade: '))
if (velo > 80):
    multa = (velo - 80) * 7
    print('Foi multado e deve pagar {:.2f}R$'.format(multa))
else:

    print('Boa vigem')