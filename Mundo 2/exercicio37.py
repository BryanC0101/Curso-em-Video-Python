#Conversor de números inteiros
from time import sleep

n = int(input('Diga um número inteiro: '))
n2 = n

print('Seu número {}'.format(n))
print('PROCESSANDO...')
sleep(2)

print('Seu número no binário é: {}'.format(bin(n)))
print('Seu número no octal é: {}'.format(oct(n)))
print('Seu número no hexadecimal é: {}'.format(hex(n)))

#while n > 0:
#    resto = n % 2
#   n = n // 2
#   print(resto, end='')
#print(' é a conversão para binário')



