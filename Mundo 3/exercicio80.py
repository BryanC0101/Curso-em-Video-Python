#ordedando sem sorted()

lista = []
ordenados = []

for c in range(0, 5):
    n = int(input('Informe o valor: '))
    lista.append(n)

for y in range(0, 5):
    ordenados.append(min(lista))
    lista.remove(min(lista))


print(ordenados)
