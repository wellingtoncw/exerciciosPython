km = float(input('Digite quantos KM tem sua viagem: '))
if km <= 200:
    preco = km * 0.50
    print('Sua viagem ficou no valor de R$ {:.2f}!'.format(preco))
else:
    preco2 = km * 0.45
    print('Sua viagem ficou no valor de R$ {:.2f}!'.format(preco2))