largura = float(input('Digite a largura da parede em mts: '))
altura = float(input('Digite a altura da parede em mts: '))
area = largura * altura
qtdade_tinta = area / 2
print('Largura: {}, Altura {}, Área {}, Qtade de litros de tinta necessários: {} '.format(largura, altura, area, qtdade_tinta))

