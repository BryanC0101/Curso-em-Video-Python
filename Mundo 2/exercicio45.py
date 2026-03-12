#Jokenpô
import emoji
import random
from time import sleep

tesoura = print(emoji.emojize('✂'))
pedra = print(emoji.emojize('🪨'))
papel = print(emoji.emojize('🧻'))


print('----Vamos jogar Jokenpô!----')
print('      Serão 3 rodadas       ')
print('       Escolha entre:       ')
print(emoji.emojize('            1: ✂'))
print(emoji.emojize('            2: 🪨'))
print(emoji.emojize('            3: 🧻'))
    
n1 = emoji.emojize('✂')
n2 = emoji.emojize('🪨')
n3 = emoji.emojize('🧻')

humanos = 0
maquina = 0

while humanos != 3 or maquina != 3:

    escolha = int(input('Sua escolha: '))
    numerosMaquina = [n1, n2, n3]
    escolhaMaquina = random.choice(numerosMaquina)



    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')



    print(escolhaMaquina, end='  +  ')



#Alternativas que ganho
    if escolha == 1 and escolhaMaquina == n3:
        print(n1)
        print('Humanos venceram essa rodada!')
        humanos += 1
    elif escolha == 2 and escolhaMaquina == n1:
        print(n2)
        print('Humanos venceram essa rodada!')
        humanos += 1
    elif escolha == 3 and escolhaMaquina == n2:
        print(n3)
        print('Humanos venceram essa rodada!')
        humanos += 1

    #Alternativas que perco
    if escolha == 1 and escolhaMaquina == n2:
        print(n1)
        print('A máquina venceu essa rodada!')
        maquina += 1
    elif escolha == 2 and escolhaMaquina == n3:
        print(n2)
        print('A máquina venceu essa rodada!')
        maquina += 1
    elif escolha == 3 and escolhaMaquina == n1:
        print(n3)
        print('A máquina venceu essa rodada!')
        maquina += 1


    #Alternativas de empate
    if escolha == 1 and escolhaMaquina == n1:
        print(n1)
        print('Empate')
    elif escolha == 2 and escolhaMaquina == n2:
        print(n2)
        print('Empate')
    elif escolha == 3 and escolhaMaquina == n3:
        print(n3)
        print('Empate')


    

    print('Placar: {} Humanos x {} Máquina'.format(humanos, maquina))

    #Para números inválidos
    if escolha < 1 or escolha > 3:
        print('Escolha um número válido')
    #---------------------------------------

    if humanos == 3:
        print('Muito bem humano, você ganhou da máquina')
        break
    elif maquina == 3:
        print('A máquina ganhou, seriam elas superiores?')
        break

   

