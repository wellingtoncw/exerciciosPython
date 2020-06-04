# divisiveis por 3
s = 0
for c in range(1, 7):
    if c % 3 == 0:
       s += c
print('A soma dos múltiplos de 3 entre 1 e 3 é de {}.'.format(s))
    #print(c)