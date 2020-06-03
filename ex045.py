#jokenpo
from random import randint
jogador = int(input('Escolha entre (Pedra, Papel e Tesoura...\n 1 - Pedra, 2 - Papel, 3 - Tesoura: '))
computador = randint(1, 3)
if jogador == 1 and computador == 1 or jogador == 2 and computador == 2 or jogador == 3 and computador == 3:
    print('VOCÊ GANHOU!')
else:
    print('VOCÊ PERDEU!')