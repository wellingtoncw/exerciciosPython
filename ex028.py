from random import randint
from time import sleep
computador = randint(0,5) #computador pensando no numero
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? ')) #jogador tentando advinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabéns!! Você conseguiu me vencer!!')
else:
    print('GANHEI! Eu pensei no número {}! e não no {}!'.format(computador, jogador))
