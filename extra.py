preco = float(input('Digite o valor do produto: R$'))
aVista = preco - (preco * 10 / 100) #10% de desconto
aPrazo = preco + (preco * 8 / 100) #08% de acréscimo
print('O produto que custa R$ {:.2f}, se for pago à vista, custará, R$ {:.2f}. Se for pago à prazo, custará R$ {:.2f}!'.format(preco, aVista, aPrazo))
