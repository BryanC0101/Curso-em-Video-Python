#Calcular quantidade de litros de tinta para a parede/cômodo

larg = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))

area = larg * alt
tinta = 2

print('Sua área é de {}m² e precisará de {} litros para pintar tudo'.format(area, area/tinta))