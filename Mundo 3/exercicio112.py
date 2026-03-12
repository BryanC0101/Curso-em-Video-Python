#Reescrevedo o leiaInt() agora com tratamento de erros e com um leiafloat()
def leiaint(num):
    integer = input(num)
    if not isinstance(num, int):
        while not isinstance(num, int):
            print('\033[31mERRO! Digite um número inteiro, por favor.\033[m')
            inteiro = input('Digite um número inteiro: ')
            if integer.isnumeric():
                integer = int(integer)
            if isinstance(num, int):
                return inteiro



inteiro = input('Digite um número inteiro: ')
leiaint(inteiro)
real = float(input('Digite um número real: '))

print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')