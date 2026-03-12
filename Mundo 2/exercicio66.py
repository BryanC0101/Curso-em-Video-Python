#Utilizando o break para parar quando necessário
s = 0
cont = 0
while True:
    n = int(input('Informe um número: (999 para parar) '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'A soma de todos os números digitados foi de {s}')
print(f'A quantidade de números digitados foi de {cont}')
