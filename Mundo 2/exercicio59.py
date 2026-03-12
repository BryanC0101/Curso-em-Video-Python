#Criando uma espécie de calculadora

print('====== Calculadora ======')

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segudno número: '))


escolha = 0

while escolha != 7:

#==================================================================================#
    print('\033[33mInforme o tipo de operação que deseja realizar: \033[m')
    print('\033[36m[1] Soma\033[m\n' 
      '\033[36m[2] Subtração\033[m\n' 
      '\033[36m[3]Multiplicação\033[m\n' 
      '\033[36m[4]Divisão\033[m\n' 
      '\033[36m[5]Maior\033[m\n' 
      '\033[36m[6]Novos números\033[m\n' 
      '\033[36m[7]Sair do programa\033[m')
#==================================================================================#

    escolha = int(input('\033[31mSua opção: \033[m'))

    if escolha == 1:
        print(print('A soma de {} + {} é igual a: {}'.format(num1, num2, num1 + num2)))

    if escolha == 2:
        print('A subtraçao de {} - {} é igual a: {}'.format(num1, num2, num1 - num2))

    if escolha == 3:
        print('A multiplicação de {} x {} é igual a: {}'.format(num1, num2, num1 * num2))

    if escolha == 4:
        print('A divisão de {} / {} é igual a: {}'.format(num1, num2, num1 / num2))

    if escolha == 5:
        print('O maior número entre {} e {} é: {}'.format(num1, num2, max(num1, num2)))

    if escolha == 6:
        escolha = 0
        print('\033[32mEscolha seus novos números: \033[m')
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segudno número: '))
        continue
    if escolha < 1 or escolha > 7:
        print('Número inválido, selecione uma das opções existentes')
print('Obrigado por utilizar o programa, volte quando precisar!')
