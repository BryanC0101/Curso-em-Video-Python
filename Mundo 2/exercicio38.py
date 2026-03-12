#Comparador de números

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O primeiro número {} é maior que {}'.format(n1, n2))
elif n2 > n1:
    print('O segundo número {} é maior que {}'.format(n2, n1))
else:
    print('Nenhum é maior nem menor, os dois números são iguais')