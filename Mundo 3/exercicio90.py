#Descobrindo a situação escolar de um aluno usando dicionários

"""nome = str(input('Qual o nome do aluno: '))
media = float(input(f'Qual a média de {nome}: '))

situacao = {
    "Nome": nome,
    "Media": media,
}

for k, v in situacao.items():
    print(f'{k} é {v}')

if media < 7:
    print(f'{situacao["Nome"]} foi reprovado')
else:
    print(f'{situacao["Nome"]} foi aprovado')
"""




#Esse próximo foi feito pelo Guanabara, copiei para ver o que errei

aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')