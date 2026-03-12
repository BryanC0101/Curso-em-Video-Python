#Par ou Impar com o computador
import random
from time import sleep
vitorias_humano = 0

while True: 
    Par_Impar = ['PAR', 'IMPAR']
    escolha_random = random.randint(1, 2)
    computador = Par_Impar[1]
    jogador = 'nada'
   
    

    if escolha_random == 1:
        #===============Par ou Impar do jogador===============
        print('===============Par ou Impar do computador===============')
        jogador = str(input('Par ou Impar? ')).strip().upper()
        #========================================================
        #===============Par ou Impar do computador===============
        print('Computador pensando...')
        sleep(1)
        if jogador == Par_Impar[0]:
            computador = Par_Impar[1]
            print('Impar')
        elif jogador == Par_Impar[1]:
            computador = Par_Impar[0]
            print('Par')
        #========================================================


    if escolha_random == 2:
        #===============Par ou Impar do computador===============
        print('Computador pensando...')
        sleep(1)
        if jogador == 'nada':
            computador = random.choice(Par_Impar)
            print(computador)

        print('===============Par ou Impar do jogador===============')   
            
        if computador == Par_Impar[1]:
            jogador = Par_Impar[0]
            print('Você ficou com PAR')
        elif computador == Par_Impar[0]:
            jogador = Par_Impar[1]
            print('Você ficou com IMPAR')    
        #========================================================

    computador_numero = random.randint(1, 10)
    humano_numero = int(input('Diga um número de 1 a 10: '))
    for c in range(1, 4):
        sleep(1)
        print(c)
    print('Já!!!!')
    sleep(0.5)
    print(f'O computador escolheu: {computador_numero}')
    print(f'Você escolheu: {humano_numero}')
    soma = computador_numero + humano_numero

    print(f'{computador_numero} + {humano_numero} é igual a: {soma}')
    print('Portanto: ')
    sleep(2)
    if jogador == Par_Impar[0] and soma % 2 == 0:
        print('PAR VENCEU!')
        print('O jogador ganhou!')
        vitorias_humano += 1
    elif computador == Par_Impar[0] and soma % 2 == 0:
        print('PAR VENCEU!')
        print('O computador ganhou!')
        break
    elif jogador == Par_Impar[1] and soma % 2 != 0:
        print('IMPAR VENCEU!')
        print('O jogador ganhou!')
        vitorias_humano += 1
    elif computador == Par_Impar[1] and soma % 2 != 0:
        print('IMPAR VENCEU!')
        print('O computador ganhou!')
        break
print('Bom, você perdeu desta vez')
print(f'Você teve {vitorias_humano} vitórias consecutivas')