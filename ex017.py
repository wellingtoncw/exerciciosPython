from math import hypot
coposto = float(input('Digite o tamanho do cateto oposto: '))
cadjacente = float(input('Digite o valor do cateto adjacente: '))
hip = hypot(coposto, cadjacente) #múdulo de match para calculo da hipotenusa
print('A hipotenusa vale {:.2f}'.format(hip))


# Método Matemática (Teorema de Pitágoras)
'''coposto = float(input('Digite o tamanho do cateto oposto: '))
cadjacente = float(input('Digite o valor do cateto adjacente: '))
hip = (coposto ** 2 + cadjacente ** 2) ** (1/2)
print('A hipotenusa vale {:.2f}'.format(hip))'''

