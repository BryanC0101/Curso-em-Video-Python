#Sequência de Fibonacci
#int(input('Digite um número inteiro: '))

n = int(input('Digite um número inteiro: '))
na = 0
naa = 0
fn = 0
termo = 0
calc = na + naa
print('{}'.format(calc), end=' ')
na = 1

while termo != (n - 1):
    naa = na
    na = calc
    calc = na + naa
    #print(calc)
    print('{}'.format(calc), end=' ')
    termo += 1
print('FIM')

  






    
