#Somando e sorteando com lista e função
import random   

numeros = []


def sorteio():
    
    numeros.append(random.sample(range(1, 11), 5))
    print('Sorteando 5 valores da lista:', end=' ')
    for c in numeros:
        for y in c:
            
            print(y, end=' ')
def soma_par():
    soma = 0
    print('Somando os valores pares ', end='')
    for c in numeros:
        for y in c:
            if y % 2 == 0:
                soma += y
                print(y, end=' ')
    print(f'temos: {soma}')
                

sorteio()
print()
soma_par()