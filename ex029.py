limite = 80;
velocidade = float(input('Digite a velocidade do carro: '))
multa = (velocidade - limite) * 7
if velocidade <= limite:
    print('Dentro do limite!')
else:
    print('MULTADO EM R$ {}!'.format(multa))