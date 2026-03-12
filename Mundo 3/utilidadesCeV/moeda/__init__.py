def aumentar(num, show=False):
    dez_porcento_up = num + (num * 0.10)
    if show == True:
        return f'R${dez_porcento_up}'
    else:
        return dez_porcento_up

def diminuir(num, show=False):
    treze_porcento_down = num - (num * 0.13)
    if show == True:
        return f'R${treze_porcento_down}'
    else:
        return treze_porcento_down

def dobro(num, show=False):
    dobrando = num * 2
    if show == True:
        return f'R${dobrando}'
    else:
        return dobrando

def metade(num, show=False):
    divisao = num / 2
    if show == True:
        return f'R${divisao}'
    else:
        return divisao

def moeda(num):
    return f'R${num}'
    
def resumo(num, porcent1, porcent2):
    print('_'*30)
    print()
    print('RESUMO'.center(30))
    print('_'*30)
    print()

    print(f'Preço analisado: R${num}')
    print(f'Dobro do preço: R${num * 2}')
    print(f'Metade do preço: R${num / 2}')
    print(f'{porcent1}% de aumento: R${num + (num * (porcent1 / 100))}')
    print(f'{porcent2}% de redução R${num - (num * (porcent2 / 100))}')
    print('_'*30)
