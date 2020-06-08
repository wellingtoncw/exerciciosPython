numero = int(input('Digite um numero: '))
t = 0
print('A TABUADA DO NÚMERO DIGITADO É: ')
print('-' * 12)
for c in range(0, 11):
    t = numero * c
    print('{} x {:2} = {}'.format(numero, c, t))
print('-' * 12)
print('FIM!!!')


