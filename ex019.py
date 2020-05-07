from random import choice
paluno = str(input('Primeiro Aluno: '))
saluno = str(input('Segundo Aluno: '))
taluno = str(input('Terceiro Aluno: '))
qaluno = str(input('Quarto Aluno: '))
lista = [paluno, saluno, taluno, qaluno]
sorteado = choice(lista) # escolhe um valor da lista
print('O aluno sorteado foi {}.'.format(sorteado))
