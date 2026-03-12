#Tabuada 3.0
while True:
    n = int(input('Gostaria de ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('='*30)
    
    for c in range(1, 11):
        mult = n * c
        print(f'{n} x {c} = {mult}')
    print('='*30)
    if n < 0:
        break
print('Obrigado por utilizar o programa, volte sempre!')