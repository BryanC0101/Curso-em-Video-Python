#Escolher ordem de apresentação de trabalhos de amenira aleatória

import random

nomes = ['Bryan', 'Vitória', 'Lucas', 'Luana']
sorteio = random.shuffle(nomes)
print('A ordem de apresentação é {}'.format(', '.join(nomes)))