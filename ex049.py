numero = int(input('Digite um numero: '))
t = 0
print('A TABUADA DO NÚMERO DIGITADO É: ')
print('-' * 12)
for c in range(0, 11):
    t = numero * c # a variavel t recebe a multiplicação do numero digitado e o contador
    print('{} x {:2} = {}'.format(numero, c, t))
print('-' * 12)
print('FIM!!!')


