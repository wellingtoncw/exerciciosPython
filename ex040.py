#media de notas
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('-=-'* 20)
print('MÉDIA DESTA UNIDADE ESCOLAR: 7.0')
print('-=-'* 20)
if media < 5:
    print('REPROVADO! Média foi {:.2f}!'.format(media))
elif media >= 5 and media <= 6.9:
    print('RECUPERAÇÃO! Média foi {:.2f}!'.format(media))
else:
    print('APROVADO! Média foi {:.2f}!'.format(media))

