import random
sorteio = random.randrange(6)
print('PENSANDO EM UM NÚMERO...')
numero = str(input('De 1 a 5, em que número eu pensei? '))
if numero == sorteio:
    print('PARABÉNS!! VOCÊ GANHOU!!')
else:
    print('VOCÊ ERROU! TENTE OUTRA VEZ! :(')
print('O número em que eu pensei foi {}'.format(sorteio))
