#Fazendo uma pancada de coisas com lista
escolha = 's'
lista = []
while escolha == 's':
    n = int(input('Informe o número: '))
    lista.append(n)
    escolha = str(input('Quer continuar? [S/N] ')).lower().strip()
    if escolha == 'n':
        break
    elif escolha == 's':
        continue
    else:
        while escolha != 's' and escolha != 'n':
            escolha = str(input('Tente novamente: [S/N] ')).lower().strip()
            if escolha == 'n':
                break
            elif escolha == 's':
                continue
lista.sort(reverse=True)
print(f'A quantidade de números digitados foram: {len(lista)}')
print(f'A lista em forma decrescente: {lista}')
if 5 in lista:
    print('Sim, o número 5 está na lista')
else:
    print('Não, o número 5 não foi digitado')