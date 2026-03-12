#ordedando numeros com listas e sorted()
lista = []
escolha = 's'
while escolha == 's':
    n = int(input('Informe um valor: '))
    if n not in lista:
        lista.append(n)
    else:
        continue
    escolha = str(input('Quer continuar? [S/N]: ')).lower().strip()   
    if escolha == 's':
        continue
    elif escolha == 'n':
        break
    else:
        escolha = str(input('Erro, adicione [S/N] para continuar: ')).lower().strip()
print(sorted(lista))
