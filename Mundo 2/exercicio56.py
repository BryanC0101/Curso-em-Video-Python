#difícil, apenas difícil

nomes = []
idades = []
generos = []

for c in range(0, 4):
    print('======== {}º Pessoa ========'.format(c + 1))
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo (M/F): '))
    
    nomes.append(nome)
    idades.append(idade)
    generos.append(sexo)

#Avaliando a média
print('=================================')
soma = 0
for y in range(0, 4):
    soma += idades[y]
calculo = soma // 4
print("A média é de {} anos".format(calculo))
print('=================================')

#Homem mais velho
print('=================================')

maior_idade = 0
posicao = -1

for r in range(len(idades)):
    if generos[r] == 'm' and idades[r] > maior_idade:
        maior_idade = idades[r]
        posicao = r

if posicao != -1:
    print('O homem mais velho é: {}'.format(nomes[posicao]))
    print('Com {} anos de idade'.format(maior_idade))
else:
    print('Não há homens na lista')

print('=================================')
#Quantas mulheres com menos de 20 anos
print('=================================')
mulheres_menos_vinte = []
menosVinte = 0
for k in range(len(idades)):
    if generos[k] == 'f' and idades[k] < 20:
        mulheres_menos_vinte.append(nomes[k])
        menosVinte += 1
print('Há {} mulher com menos de 20 anos'.format(menosVinte))
print('Sendo ela(s): {}'.format(', '.join(mulheres_menos_vinte)))
print('=================================')

    



