#Ler um ângulo e pegar seu seno, coseno e tangente

import math

number = float(input('Diga o ângulo: '))
radians = math.radians(number)
print('Seno é {:.2f}, coseno é {:.2f} e tangente é {:.2f}'.format(math.sin(radians), math.cos(radians), math.tan(radians)))