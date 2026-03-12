#Comparar pesos
peso = 0
resultadoMaior = 0
pesoLista = []
for c in range(0, 5):
    peso = float(input('Digite o peso: '))
    print('------------------')
    if peso > resultadoMaior:
        resultadoMaior = peso
    else:
        resultadoMaior = resultadoMaior
    pesoLista.append(peso)


print('O maior peso é: {}Kg'.format(resultadoMaior))
print('O menor peso é: {}Kg'.format(min(pesoLista)))
 


