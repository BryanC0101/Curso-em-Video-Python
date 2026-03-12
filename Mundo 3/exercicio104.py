#Fazendo um input que só aceita números

def leiaint(numero):
    teste = input(numero).strip()
    if teste.isnumeric():
        print(f'\033[32mVocê digitou o número {teste}\033[m')
    else:
        while not teste.isnumeric():
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            teste = input('Digite um número: ').strip()
            if teste.isnumeric():
                print(f'\033[32mVocê digitou o número {teste}\033[m')
                break

n = leiaint('Digite um número: ')