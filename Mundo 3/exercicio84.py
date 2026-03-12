#aprendendo a colocar listas dentro de litas
lista = []
lista_maior = []
lista_pesados = []
lista_leves = []
count = 1
escolha = 's'
while escolha == 's':
    nome = str(input(f'Informe o {count}º nome: ')).strip()
    peso = float(input('Digite o peso da pessoa: '))
    lista.append(nome)
    lista.append(peso)
    lista_maior.append(lista[:])
    lista.clear()
    escolha = str(input('Deseja continuar? [S/N] ')).lower().strip()
    if escolha == 's':
        count += 1
        continue
    elif escolha == 'n':
        break
    else:
        while escolha != 's' and escolha != 'n':
             escolha = str(input('Tente novamente, deseja continuar? [S/N] ')).lower().strip()

print(f'A quantidade de pessoas cadastradas foi de: \033[31m{count}\033[m')
pesado = lista_maior[0][1]
leve = lista_maior[0][1]

for c in lista_maior:
    if c[1] > pesado:
        pesado = c[1]
    if c[1] < leve:
        leve = c[1]
    
for y in lista_maior:
    if y[1] == pesado:
        lista_pesados.append(y[0])

for g in lista_maior:
    if g[1] == leve:
        lista_leves.append(g[0])


print(f'O \033[32mmaior\033[m peso foi {pesado}, sendo: {lista_pesados}')
print(f'O \033[33mmenor\033[m peso foi {leve}, sendo: {lista_leves}')