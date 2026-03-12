#Guardando valores na tupla pelo teclado
noves = 0
tres = 0
pares = ()
numeros = tuple(int(input('Número: ')) for _ in range(0, 4))
print(numeros)
for y in range(0, 4):
    if numeros[y] == 9:
        noves += 1
if 3 in numeros:
    tres = numeros.index(3)

for c in range(0, 4):
    if numeros[c] % 2 == 0:
        pares += (numeros[c],)
print(f'A quantidade de números \033[31m9\033[m foram de: \033[33m{noves}\033[m')
if 3 in numeros:
    print(f'O primeiro número \033[31m3\033[m está na posição \033[33m{tres + 1}\033[mº')
else:
    print('O valor três não foi encontrado em nenhuma posição')
print(f'Esse são os números pares: \033[33m{pares}\033[m')