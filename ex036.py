#emprestimo bancario
valorcasa = float(input('Qual o valor da Casa R$: '))
salario = float(input('Quanto você ganha por mês R$: '))
anos = int(input('Deseja parcelar em quantos anos? '))
prestacao = valorcasa / anos
if prestacao <= (salario * 30/100):
    print('Sua prestação será no valor de: {}, durante {} anos!'.format(prestacao, anos))
else:
    print('PROPOSTA NEGADA! O valor da sua prestação esta maior do que 30% de seu salário.\n Valor da Prestação: {:.2f}. 30% do Salário: {:.2f}.'.format(prestacao, (salario * 30/100)))

