#Tabuada 2.0

n = int(input('Escolha o número a ser multiplicado: '))

for c in range (1, 11):
    calc = n * c
    print('{} x {} = {}'.format(n, c, calc))

