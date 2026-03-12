#Verificar se palavra é um palíndromo

palavra = input('Digite a frase: ').strip().replace(' ', '')

invertido = palavra[::-1]

print('O inveso da palavra {} é {}'.format(palavra, invertido))

if invertido == palavra:
    print('É um palíndromo')
else:
    print('Não, não é palíndromo')
