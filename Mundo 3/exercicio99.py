#Pegando o maior valor de parâmetros com função

def maior(*parametro):
    lista = []
    lista.append(parametro)
    print('-=-'*30) 
    print('Analisando os valores passados...')
    for c in lista:
        print(f'{c} Foram informados {len(parametro)} valores ao todo.', end='')
        print()
        print(f'O maior valor foi {max(parametro)}', )
    print('-=-'*30)

maior(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
maior(4, 190, 412, 23, 756, 32, 123, 45, 100)
maior(1, 8 , 85, 42, 45, 86)
maior(1)
maior(0)