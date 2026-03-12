#Fazendo uma matriz com listas
lista = []
coluna_a = [0, 0 ,0]
coluna_b = [0, 0, 0]
coluna_c = [0, 0, 0]
lista.append(coluna_a)
lista.append(coluna_b)
lista.append(coluna_c)
soma = 0
soma3coluna = 0
for c in range(0, 3):
    for y in range(0, 3):
        n = int(input(f'Digite o valor [{c}, {y}] de sua matriz: '))
        lista[c][y] = n
        if y == 2:
            soma3coluna += n
        

for linha in lista:
    for elemento in linha:
        if elemento % 2 == 0:
            soma += elemento
        print(f'[ {elemento} ]', end=" ")
    print()

print(f'A soma de todos os números pares é: {soma}')
print(f'A soma dos números da terceira coluna é: {soma3coluna}')
print(f'O maior valor da segunda linha é: {max(coluna_b)}')