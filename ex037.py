#bases numéricas
numero = int(input('Digite um número inteiro qualquer: '))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('O número {} convertido para BINÁRIO é igual a {}.'.format(numero, bin(numero)[2:])) # [2:] SERVE PRA FATIAMENTO. A STRING COMEÇA A PARTIR DA SEGUNDA POSIÇÃO
elif opcao == 2:
    print('O número {} convertido para OCTAL é igual a {}.'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('O número {} convertido para HEXADECIMAL é igual a {}.'.format(numero, hex(numero)[2:]))
else:
    print('OPÇÃO INVÁLIDA!')



