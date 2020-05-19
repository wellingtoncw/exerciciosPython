ano = int(input('Digite um ano: '))
if ano % 4 == 0 & ano % 100 != 0:
    print('Bissexto')
else:
    print('Não Bissexto')
