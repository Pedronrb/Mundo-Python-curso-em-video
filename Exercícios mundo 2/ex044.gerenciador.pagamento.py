print('{:=^40}'.format(' Findout Store '))
preco = float(input('Preço das compras: R$'))
print(''' FORMAS DE PAGAMENTO 
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10/100)
elif opcao == 2:
    total = preco - (preco * 5/100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20/100)
    totalParc = int(input('Quantas vezes? '))
    parcela = total / totalParc
    print('Sua compra será parcela em {}x de R${:.2f} COM JUROS'.format(totalParc, parcela))
else:
    total = preco
    print('Opção inválida de pagamento. Tente novamente!')
    
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))
