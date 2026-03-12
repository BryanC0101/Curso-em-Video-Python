#Criando uma função de ajuda do Python
from time import sleep
def ajuda():
    escolha = ''
    while True:
        print('\033[97;44m' + '~' * 25 + ' ' * 100 + '\033[m')
        print('\033[97;44m' + 'SISTEMA DE AJUDA PyHELP' + ' ' * 102 + '\033[m')
        print('\033[97;44m' + '~' * 25 + ' ' * 100 + '\033[m')

        funcao = str(input('Função ou Biblioteca > ')).strip().lower()
        if funcao == 'fim':
            print('\033[97;41m' + '~' * 25 + ' ' * 100 + '\033[m')
            print('\033[97;41m' + 'ATÉ LOGO' + ' ' * 117 + '\033[m')
            print('\033[97;41m' + '~' * 25 + ' ' * 100 + '\033[m')
            break
        else:
            print('\033[97;42m' + '~' * 40 + ' ' * 85 + '\033[m')
            print('\033[90;42m' + f" Acessando o manual do conteúdo '{funcao}' " + ' ' * 87 + '\033[m')
            print('\033[97;42m' + '~' * 40 + ' ' * 85 + '\033[m')
            sleep(1)
            print('\033[30;47m', end='')
            help(funcao)
            print('\033[m')

ajuda()

