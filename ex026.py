frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A')+1)) # find retorna a posição em que foi encontrado a primeira vez
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A')+1))

