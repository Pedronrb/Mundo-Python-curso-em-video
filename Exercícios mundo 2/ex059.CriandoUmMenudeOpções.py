from time import sleep
#Entrada
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print(20*'-==-')
print()

#Processo
opção = 0
while opção != 5:

    print('   [ 1 ] Somar\n   [ 2 ] Multiplicar\n   [ 3 ] Maior\n   [ 4 ] Novos números\n   [ 5 ] Sair do programa' )
    print()
    opção = int(input((f'>>>>> Qual é a sua opção? ')))
    print()
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma} ')
        print()
    elif opção == 2:
        multi = n1 * n2
        print(f'A multiplicação entre {n1} + {n2} é {multi} ')
        print()
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior} ')
        print()
    elif opção == 4:
        n1 = int(input('Digite o primeiro novo número: '))
        n2 = int(input('Digite o segundo novo número: '))
        print()
    elif opção == 5:
        print('Finalizado.....')
        print("-=-"*20)
    else:
        print('Opção inválida. Tente novamente.')
        print("-=-"*20)
        sleep(2)
print('Fim do programa')
