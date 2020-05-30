from datetime import date
ano = int(input('Que ano você quer analisar? Coloque 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year # da data atual (date.today()) pega o ano
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é Bissexto!'.format(ano))
else:
    print('O ano de {} Não Bissexto!!'.format(ano))
