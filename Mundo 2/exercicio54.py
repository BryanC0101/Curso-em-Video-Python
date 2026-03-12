#Quais são maiores de idade
from datetime import datetime

dataAtual = datetime.now().year

listaMaiores = list()
listaMenores = list()
print('Coloque 7 nomes e suas datas de nascimento abaixo:')

for c in range(0, 7):
    nomePessoa = input('Digite o nome da pessoa: ')
    anoPessoa = int(input('Digite o ano de nascimento da pessoa: '))
    idade = dataAtual - anoPessoa
    if idade >= 21:
        listaMaiores.append(nomePessoa)
    elif idade < 21:
        listaMenores.append(nomePessoa)
    print('-----------------------------')
print('Os nomes que são maiores são: ')
print(", ".join(listaMaiores))
print('Os nomes que são menores são: ')
print(", ".join(listaMenores))

print('Há {} menores e {} maiores'.format(len(listaMenores), len(listaMaiores)))