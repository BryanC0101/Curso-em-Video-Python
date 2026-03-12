import moeda2

n = float(input('Digite o preço: R$: '))
print(f'A metade de {moeda2.moeda(n)} é {moeda2.metade(n)}')
print(f'O dobri de {moeda2.moeda(n)} é {moeda2.moeda(moeda2.dobro(n))}')
print(f'Aumentando 10% de {moeda2.moeda(n)}, temos {moeda2.moeda(moeda2.aumentar(n))}')
print(f'Reduzindo 13% de {moeda2.moeda(n)}, temos {moeda2.moeda(moeda2.diminuir(n))}')
