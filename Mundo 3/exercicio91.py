#Jogando dados com random utilziando dicionários
#parte do rankin feito com ajuda do curso em video
import random
from operator import itemgetter
dado = {}
ranking = []
count = 1
print('Valores sorteados: ')
for c in range(1, 5):
    dado[f'jogador{c}'] = random.randint(1, 6)
for k, v in dado.items():
    print(f'O {k} jogou {v}')
print('Ranking dos jogadores: ')

ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}.')