#teorema de pitagoras

import math

catoposto = float(input('Qual o cumprimento do cateto oposto? '))
catadjacente = float(input('Qual o cumprimento do cateto adjacente? '))

hipotenusa = math.hypot(catoposto, catadjacente)

print(f"{hipotenusa:.2f}", 'ou {}'.format(hipotenusa))