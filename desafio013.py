salario = float(input('Digite o seu salário R$: '))
aumento = salario * 0.15
novo_salario = salario + aumento
print('Seu salário de R$: {:.2f}, com o aumento de R$ {:.2f}, agora vale R$: {:.2f}'.format(salario, aumento, novo_salario))
