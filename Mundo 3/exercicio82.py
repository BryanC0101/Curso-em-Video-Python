#Organizando pares e ímpares em listas extras

lista = []
lista_pares = []
lista_impares = []
escolha = 's'
while escolha == 's':
    n = int(input('Informe o número: '))
    lista.append(n)
    escolha = str(input('Quer continuar? [S/N]')).lower().strip()
    if escolha == 's':
        continue
    elif escolha =='n':
        break
    else:
        while escolha != 's' and escolha != 'n':
            escolha = str(input('Erro, digite uma das duas opções [S/N] ')).lower().strip()
            if escolha == 'n':
                break
            elif escolha == 's':
                continue
for c in lista:
    if c % 2 == 0:
        lista_pares.append(c)
    elif c % 2 == 1:
        lista_impares.append(c)
print('-'*20)
print(f'A lista original é: \033[32m{lista}\033[m')
print('-'*20)
print(f'A lista apenas dos números \033[33mpares\033[m serão: \033[32m{lista_pares}\033[m')
print(f'A lista apenas dos números \033[31mímpares\033[m são: \033[32m{lista_impares}\033[m')