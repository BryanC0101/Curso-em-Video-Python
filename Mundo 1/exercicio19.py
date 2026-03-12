#Escolha aleatória de quem apagará o quadro

import random

nomes = ['Bryan', 'Vitória', 'Lucas', 'Luana']
escolha = random.choice(nomes)

print('O professor escolherá {} para apagar o quadro'.format(escolha))