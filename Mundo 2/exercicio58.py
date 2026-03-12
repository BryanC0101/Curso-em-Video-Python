#Jogo de adivinhação 2.0
import random

humano = None
maquina = random.randint(1, 10)
placar = 10
numeros_jogados = []


print('========= Jogo de adivinhções 2.0 =========')

while humano != maquina:

    humano = int(input('Digite um número de 1 a 10: '))
    numeros_jogados.append(humano)
    placar -= 1

    while humano != maquina:
        if humano > maquina:
            print('Menos, tente outra vez...')
        elif humano < maquina:
            print('Mais, tente outra vez...')
        humano = int(input('Digite outro número entre os {} restantes: '.format(placar)))
        placar -= 1
        numeros_jogados.append(humano)
        if placar < 0:
            break
        else:
            continue
else:
    print('======== Resultado =======')
    print('Parabéns, você acertou o número da máquina!')
    print('Você precisou de {} chances para acertar!'.format(10 - placar))
    print('Essas foram suas escolhas:', *numeros_jogados)