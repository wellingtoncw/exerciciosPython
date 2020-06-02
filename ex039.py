#alistamento militar
from datetime import date
nascimento = int(input('Informe seu ano de nascimento: '))
ano = date.today().year
idade = ano - nascimento
if idade < 18:
    print('Ainda faltam {} anos pro seu alistamento!'.format(18-idade))
elif idade == 18:
    print('Está na hora de você se alistar!!!')
else:
    print('Já passaram {} anos do seu alistamento!!'.format(idade-18))
