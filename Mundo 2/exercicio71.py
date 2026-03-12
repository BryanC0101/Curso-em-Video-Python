#Criando um saque de caixa eletrônico
print('=============== Caixa Eletrônico ===============')

saque = int(input('Quantos você quer sacar? '))
cont50 = 0
cont20 = 0
cont10 = 0
cont1 = 0



while (saque - 50) >= 0:
    saque -= 50
    cont50 += 1
    if (saque - 50) < 0:
        break

while (saque - 20) >= 0:
    saque -= 20
    cont20 +=1
    if (saque - 20) < 0:
        break

while (saque - 10) >= 0:
    saque -= 10
    cont10 +=1
    if (saque - 10) < 0:
        break

while (saque - 1) >= 0:
    saque -= 1
    cont1 +=1
    if (saque - 1) < 0:
        break


if cont50 > 0:
    print(f'\033[31m{cont50}\033[m cédulas de cinquenta reais')
if cont20 > 0:
    print(f'\033[31m{cont20}\033[m cédulas de vinte reais')
if cont10 > 0:
    print(f'\033[31m{cont10}\033[m cédulas de dez reais')
if cont1 > 0:
    print(f'\033[31m{cont1}\033[m cédulas de 1 real')



#cédulas de 50, 20, 10, 1 real