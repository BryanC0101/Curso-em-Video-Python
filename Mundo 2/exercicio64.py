#Somando números incluidos no while
n = 0
soma = 0
digitados = 0
while n != 999:
    n = int(input('Informe seu número: '))
    if n != 999:
        soma += n
        digitados += 1
    else:
        break
print('A soma de todos os números foi de: {}'.format(soma))
print('A quantidade de números digitados foi de: {}'.format(digitados))