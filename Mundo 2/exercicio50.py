#Calcular apenas valores pares em for

calc = 0
quantidade = 0
print('Digite 6 números inteiros: ')
for c in range (1, 7):
    n = int(input('Digite o número: '))
    if n % 2 == 0:
        calc += n
        quantidade += 1
    else:
        calc += 0
print('Você informou {} números pares e a soma foi de {}'.format(quantidade, calc))