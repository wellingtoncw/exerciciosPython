
nome = str(input('Digite seu nome completo: ')).strip() # metodo pra excluir os espaços da string
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' '))) # len - metodo para contar a quantidade de caracteres. count - método para contar os que está entre aspas
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' '))) # find é o método de buscar e retorna a quantidade de caracteres
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0]))) #separa pra pegar o indice 0 e len pra contar quantos carecteres