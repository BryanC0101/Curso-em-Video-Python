#Fazendo um contador com função
from time import sleep

def contador(x, y, z):
    if z == 0:
        z = 1
        
    if z < 0:
         z = abs(z)
    
    if x > y:
        z = -z
        print(f'Contagem de {x} até {y} em {abs(z)} em {abs(z)}: ')
    else:
        print(f'Contagem de {x} até {y} em {z} em {z}: ')

    
    
    for c in range(x, y + z, z):
        if (z > 0 and c > y) or (z < 0 and c < y):
            break
        sleep(0.25)
        print(c, end=' ')
    print()

contador(1, 10, 1)
contador(10, 0, 2)

print('Personalize uma contagem: ')
inicio = int(input('Início: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))
contador(inicio, fim, passo)