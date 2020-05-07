from random import shuffle
paluno = str(input('Primeiro Aluno: '))
saluno = str(input('Segundo Aluno: '))
taluno = str(input('Terceiro Aluno: '))
qaluno = str(input('Quarto Aluno: '))
lista = [paluno, saluno, taluno, qaluno]
shuffle(lista) # embaralha os valores da lista
print('A ordem de apresentação será: {},.'.format(lista))
