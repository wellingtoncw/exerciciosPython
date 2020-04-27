import random

comida = str(input('Olá, Qual é seu prato predileto? '))
andar = random.randrange(333)

print('Você escolheu {}!!!'.format(comida))
print('-' * 15)
print('MES 1')
print('VOCÊ ESTÁ NO: {}º ANDAR! ÓBVIO!'.format(andar))
print('-' * 15)