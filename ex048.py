# soma dos impares multiplos de 3
s = 0
for c in range(1, 501):
  if c % 3 == 0 and c % 2 != 0:
    s += c # soma = soma + c
    print(c)
print('A SOMA dos múltiplos de 3 entre 1 e 500 é de {}.'.format(s))