numero = int(input('Digite o número para a conversão: '))
print('[1] para Binário\n[2] para Octal\n[3] para Hexadecimal')
opcao = int(input('Digite a opção da conversão: '))
if opcao == 1:
    print('{} convertido para binário é {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para octal é {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é {}'.format(numero, hex(numero)))
else: 
    print('Opção inválida')