from math import radians, cos, sin, tan
angulo = float(input('Digite um ângulo: '))
seno = sin(radians(angulo)) #lendo de tras pra frente, converte o angulo digitado para radianos e calcula o senho e guarda na variavel seno.
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}.'.format(angulo, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}.'.format(angulo, cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}.'.format(angulo, tangente))
