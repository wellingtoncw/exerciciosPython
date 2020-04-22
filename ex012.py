preco = float(input('Digite o preço do produto R$: '))
#desconto = preco * 0.05
#novo_valor = preco - desconto
novo = preco - (preco * 5 / 100)
print('O produto que custava R$: {:.2f}, aplicando o desconto de 5%, agora vale R$: {:.2f}!'.format(preco, novo))

