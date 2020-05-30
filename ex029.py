limite = 80;
velocidade = float(input('Digite a velocidade do carro: '))
multa = (velocidade - limite) * 7
if velocidade <= limite:
    print('Tenha um Bom dia! Dirija com segurança!')
else:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h e deverá pagar uma multa de R$ {}!'.format(multa))