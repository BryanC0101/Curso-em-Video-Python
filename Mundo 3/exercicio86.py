#Fazendo uma matriz com listas
lista = []
coluna_a = [0, 0 ,0]
coluna_b = [0, 0, 0]
coluna_c = [0, 0, 0]
lista.append(coluna_a)
lista.append(coluna_b)
lista.append(coluna_c)
for c in range(0, 3):
    for y in range(0, 3):
        n = int(input(f'Digite o valor [{c}, {y}] de sua matriz: '))
        lista[c][y] = n

for linha in lista:
    for elemento in linha:
        print(f'[ {elemento} ]', end=" ")
    print()

