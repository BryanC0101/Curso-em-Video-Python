#Mostrando ou não fatorial com função e parâmetros opcionais

def fatorial(numero, show=True):

    """
    Calcula o fatorial de um número:
    numero (int): O número a ser calculado na fatoração
    show (bool): parâmetro opcional, usado para mostrar ou não o processo da conta

    Retorna:
    int: resultado do fatorial

    """


    fat = numero
    if show:
        print(numero, end=' ')
    for c in range(numero - 1, 1, -1):
        fat *= c
        if show:
            print('x', c, end=' ')
    if show:
        print('= ', end='')
    return fat

help(fatorial)



n = int(input('Digite um número para saber seu fatorial: '))
escolha = int(input('Quer ver o cálculo? [Sim = 1/ Não = 2] '))
if escolha == 1:
    print(fatorial(n, True))
elif escolha == 2:
    print(fatorial(n, False))
else:
    print('Tente novamente!')