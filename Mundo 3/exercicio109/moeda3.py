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
    