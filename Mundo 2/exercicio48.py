#Soma dos ímpares multiplos de três num intervalo de 1 e 500

soma = 0

for c in range (1, 500):
    if c % 2 != 0 and c % 3 == 0:
        soma = soma + c
print('A soma de todos os números ímpares e múltiplos de três entre 1 e 500 é: {}'.format(soma))
