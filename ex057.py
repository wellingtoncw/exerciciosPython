sexo = str(input('Digite seu sexo:  [M/F]: ')).strip().upper()[0] # pegando a primeira letra do que for digitado ( tirando os espaços e passando pra maiusculo
while sexo not in 'MmFf':
    sexo = str(input('Dados Inválidos! Por favor, digite seu sexo:  [M/F]: ')).strip().upper()[0]
print('Seu sexo é do tipo {} e foi registrado com Sucesso!'.format(sexo))