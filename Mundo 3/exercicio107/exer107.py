import moeda1

n = float(input('Digite o preço: R$: '))
print(f'A metade de {n} é {moeda1.metade(n)}')
print(f'O dobri de {n} é {moeda1.dobro(n)}')
print(f'Aumentando 10% de {n}, temos {moeda1.aumentar(n)}')
print(f'Reduzindo 13% de {n}, temos {moeda1.diminuir(n)}')
