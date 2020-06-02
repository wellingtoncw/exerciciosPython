#IMC
from math import exp
peso = float(input('Qual é o seu peso: '))
altura = float(input('Qual é a sua altura: '))
imc = peso / (altura * altura)
print('Seu IMC é de {:.2f}!'.format(imc))
if imc < 18.5:
    print('Você está Abaixo do Peso!')
elif imc >= 18.5 and imc <25:
    print('Você está no Peso Ideal!')
elif imc >= 25 and imc < 30:
    print('Você está com SobrePeso!')
elif imc >= 30 and imc < 40:
    print('Você está com Obesidade!')
else:
    print('Você está com Obesidade Mórbida!')
