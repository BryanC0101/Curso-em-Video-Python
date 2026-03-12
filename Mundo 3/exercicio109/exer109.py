import moeda3

n = float(input('Digite o preço: R$: '))
print(f'A metade de {moeda3.moeda(n)} é {moeda3.metade(n, False)}')
print(f'O dobri de {moeda3.moeda(n)} é {moeda3.dobro(n, True)}')
print(f'Aumentando 10% de {moeda3.moeda(n)}, temos {moeda3.aumentar(n, True)}')
print(f'Reduzindo 13% de {moeda3.moeda(n)}, temos {moeda3.diminuir(n, True)}')
