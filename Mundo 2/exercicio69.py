#Lendo dados de diferentes pessoas

cont = 1
masculino = 0
feminino = 0
lista_idades = []
maiores_18 = 0
mulheres_menos20 = 0

while True:
    idade = int(input(f'Digite a idade da {cont}º pessoa: '))
    lista_idades.append(idade)
    sexo = str(input(f'Informe o sexo da {cont}º pessoa: [M/F] ')).strip().upper()

    while sexo != 'F' and sexo != 'M':
        sexo = str(input(print('Digite uma das opções válidas [M/F] '))).strip().upper()
    if sexo == 'M':
        masculino += 1
    elif sexo == 'F':
        feminino += 1

    if sexo == 'F' and idade < 20:
        mulheres_menos20 += 1
    
    
    if lista_idades[cont - 1] > 18:
        maiores_18 += 1


    cont += 1
    

   
    print('Deseja cadastrar mais pessoas? [S/N] ')
    escolha = str(input('Digite: ')).strip().upper()
    if escolha == 'S':
        continue
    elif escolha == 'N':
        print('Obrigado por utilizar o programa!')
        break
    while escolha != 'S' and escolha != 'N':
        escolha = str(input('Digite uma das opções válidas [S/M] ')).strip().upper()

    

    

print(f'A quantidade de maiores de 18 anos são: {maiores_18}')
print(f'A quantidade de homens cadastrados foi de: {masculino}')
print(f'A quantidade de mulheres com menos de 20 anos foi de: {mulheres_menos20}')