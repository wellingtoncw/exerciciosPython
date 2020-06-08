frase = str(input('Digite uma frase: ')).strip().upper() #tira os espaços e passa pra maiusculo
palavras = frase.split() #separa a frase digitada em palavras
junto = ''.join(palavras) # junta todas as palavras retirando os espaços
inverso = ''
#outra forma de fazer: inverso = junto[::-1]
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada não é um PALÍNDROMO!')



# A torre da derrota
