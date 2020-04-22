largura = float(input('Digite a largura da parede em mts: '))
altura = float(input('Digite a altura da parede em mts: '))
area = largura * altura
qtdade_tinta = area / 2
print('Largura: {}, Altura {}, Área {}m! \nQtade de litros de tinta necessários: {}l de tinta '.format(largura, altura, area, qtdade_tinta))

