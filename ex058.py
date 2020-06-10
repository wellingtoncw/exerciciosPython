from random import randint
from time import sleep
computador = randint(0, 10)
print('Sou seu computador...')
sleep(2)
print('Acabei de pensar em um número entre 0 e 10...')
sleep(2)
print('Será que você consegue advinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente outra vez.')
        elif jogador > computador:
            print('Menos... Tente outra vez.')
print('Acertou com {} palpites!'.format(palpites))
