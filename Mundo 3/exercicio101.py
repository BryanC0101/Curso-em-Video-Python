#Usando função e afíns para ver se alguém vota ou não
from datetime import datetime

def voto(ano_nascimento):
    idade = ano_atual - ano_nascimento

    if idade >= 18 and idade < 65:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    elif (idade < 18 and idade >= 16) or (idade >= 65):
        print(f'Com {idade} anos: VOTO OPCIONAL')
    elif idade < 16 and idade > 0:
        print(f'Com {idade} anos: NÃO VOTA')
    else:
        print('Coloque uma idade válida')

ano_atual = datetime.now().year
ano_nascimento = int(input('Digite seu ano de nascimento: '))

voto(ano_nascimento)


