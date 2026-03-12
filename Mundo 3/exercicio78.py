#Guardando números em uma lista e mostrando maior, menor, e posição deles
lista = []
pos_maior = []
pos_menor = []


for c in range(1, 6):
    n = int(input(f'Informe o {c}º número: '))
    lista.append(n)


for indice, valor in enumerate(lista):
    if valor == max(lista):
        pos_maior.append(indice)
    if valor == min(lista):
        pos_menor.append(indice)
    

print(f'Você digitou os valores: {lista}')
print(f'O maior valor foi: {max(lista)} nas posições: {pos_maior}º')
print(f'O menor valor foi: {min(lista)} nas posições: {pos_menor}º')
