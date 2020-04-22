preco = float(input('Digite o preço do produto R$: '))
desconto = preco * 0.05
novo_valor = preco - desconto
print('O produto que custava R$: {:.2f}, aplicando o desconto de R$: {:.2f}, agora vale R$: {:.2f}!'.format(preco, desconto, novo_valor))

