#valor a ser pago em um produto
valor = float(input('Digite o valor a ser pago R$: '))
condicao = int(input('Escolha a condição de pagamento:\n 1 - À vista no Dinheiro, 2 - À vista no Cartão, 3 - Em até 2x no Cartão, 4 - 3x ou mais no Cartão: '))
if condicao == 1:
    valor = valor - ( valor * 10/100)
    print('\nNa condição (À vista no Dinheiro), você pagará R${:.2f}'.format(valor))
elif condicao == 2:
    valor = valor - (valor * 5/500)
    print('Na condição (À vista no Cartão), você pagará R${:.2f}.'.format(valor))
elif condicao == 3:
    print('Na condição (Em até 2x no Cartão), você pagará R${:.2f} em até 2x de R${:.2f}.'.format(valor, valor/2))
else:
    valor = valor + (valor * 20/100)
    print('Na condição (3x ou mais no Cartão), você pagará R${:.2f}.'.format(valor))
