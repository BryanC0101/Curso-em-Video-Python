#Calcular valor a pagar da viagem

distancia = int(input('Digite a distância da viagem em Km: '))

if distancia <= 200:
    valor = distancia * 0.50
elif distancia > 200:
    #valor = (distancia * 0,50) + [(distancia - 200) * 0,45]
    valor = distancia * 0.45

print('Você terá que pagar: R${:.2f}'.format(valor))