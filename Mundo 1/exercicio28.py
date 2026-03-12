# Jogo de adivinhações python
import random
from time import sleep

randomN = random.randint(1, 5)

while True:
    n = int(input('Tente adivinhar o número de 1 a 5: '))
    print('PROCESSANDO...')
    sleep(3)
    if n == randomN:
        print('Parabéns, você acertou o número!')
    else:
        print('Você errou, o número era o {} e não {}, tente outra vez!'.format(randomN, n))

    yesno = str(input('Quer recomeçar? s/n')).lower()
    if yesno == 's':
        randomN = random.randint(1, 5)
        continue
    elif yesno == 'n':
        print('Até mais!')
    break
