#lendo número e mostrando seu fatorial


#Modelo utilizando WHILE
n = int(input('Digite o número para ver seu fatorial: '))
nAgain = n
fatorial = n -1
calc = 0
adicionador = n

while fatorial != 1 and fatorial > 1:
    calc = adicionador * fatorial
    adicionador = calc
    print(calc)
    n -= 1
    fatorial -= 1
print('O resultado fatorial de {}! é: {}'.format(nAgain, adicionador))


#Modelo utilizando FOR
n = int(input('Digite o número para ver seu fatorial: '))
nAgain = n
calc = 0
for c in range(n, 1, -1):
    calc = n * (c-1)
    n = calc
    calc = n
print('O resultado do fatorial de {}! é: {}'.format(nAgain, n))
