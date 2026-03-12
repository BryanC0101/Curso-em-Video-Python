#Colocando lista dentro de lista e separando pares e ímpares
#Fiz errado, era apenas com 1 lista colocando 2 listas dentro, mas vou deixar só por que não
#quero fazer agora
lista = []
pares = []
impares = []
lista.append(pares)
lista.append(impares)
for c in range(1, 8):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 == 1:
        impares.append(n)

print(f'Os valores pares são: {sorted(pares)}')
print(f'Os valores ímpares são: {sorted(impares)}')




  