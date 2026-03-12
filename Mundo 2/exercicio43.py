#Calcula Índice de Massa Corpórea

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)

print('{:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do PESO IDEAL')
elif imc >= 18.5 and imc <= 25:
    print ('Você esta no PESO IDEAL!')
elif imc > 25 and imc <= 30:
    print('Você está em SOBREPESO')
elif imc > 30 and imc < 40:
    print('Você está em OBESIDADE')
elif imc > 40:
    print('Você está em OBESIDADE MÓRBIDA')