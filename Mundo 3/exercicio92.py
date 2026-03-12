#Lendo uma pancada de coisas com dicionário
from datetime import datetime
ano_atual = datetime.now().year


dicionario = {}
dicionario['nome'] = str(input('Nome: '))
dicionario['idade'] = ano_atual - (int(input('Ano de nascimento: '))) 
dicionario['ctps'] = int(input('CTPS: \033[31m[0 não tem]\033[m '))
if dicionario['ctps'] > 0:
    dicionario['contratacao'] = int(input('Ano de contratação: '))
    dicionario['salario'] = float(input('Salário: '))
    if ano_atual - dicionario['contratacao'] >= 35:  
        dicionario['aposentadoria'] = 'Aposetado'
    else:
        dicionario['aposentadoria'] = 35 - (ano_atual - dicionario['contratacao']) + dicionario['idade']
print()
print('-=-'*20)
print()
for k, v in dicionario.items():
    print(f'{k} tem o valor {v}')
