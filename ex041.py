#categoria natação
from datetime import date
nascimento = int(input('Digite seu ano de nascimento: '))
ano = date.today().year
idade = ano - nascimento
if idade <= 9:
    print(idade, 'anos')
    print('MIRIM!')
elif idade > 9 and idade <= 14:
    print(idade, 'anos')
    print('INFANTIL!')
elif idade > 14 and idade <= 19:
    print(idade, 'anos')
    print('JUNIOR!')
elif idade > 19 and idade <= 20:
    print(idade, 'anos')
    print('SÊNIOR!')
else:
    print(idade, 'anos')
    print('MASTER!')

