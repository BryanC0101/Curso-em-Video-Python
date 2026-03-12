"""#Ajudando com palpites na Mega Sena
import random
from time import sleep
linha1 = [0, 0 ,0, 0, 0 ,0]
print('-=-'*20)
print('Jogando na MEGA SENA'.center(60))
print('-=-'*20)

n = int(input('Quantos números você quer que sejam sorteados? '))
print(f'-=-=-=-=- SORTEANDO {n} JOGOS -=-=-=-=-')
for c in range(0, n):
    for y in range(0, 6):
        linha1[y] = random.sample(range(1, 61), 1)
    sleep(1)
    print(f'Jogo {c+1}: ', end='')
    print(linha1)
print('-=-=-=-=-=-=-=-=--=-=-=-=-Boa Sorte-=-=-=-=-=-=-=-=--=-=-=-=-')
        """



#Esse segundo foi feito com ajuda do Chat-GPT, o primeiro 95% fui eu, mas teve problemas com repetição
#de números
#Ajudando com palpites na Mega Sena
import random
from time import sleep
print('-=-'*20)
print('Jogando na MEGA SENA'.center(60))
print('-=-'*20)

n = int(input('Quantos números você quer que sejam sorteados? '))
print(f'-=-=-=-=- SORTEANDO {n} JOGOS -=-=-=-=-')
for c in range(n):
    jogo = random.sample(range(1, 61), 6)
    jogo.sort()
    sleep(1)
    print(f'Jogo {c+1}: {jogo}')
print('-=-=-=-=-=-=-=-=--=-=-=-=-Boa Sorte-=-=-=-=-=-=-=-=--=-=-=-=-')


