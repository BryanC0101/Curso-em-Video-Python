#Vai se alistar ou não?
from datetime import datetime

idade = int(input('Digite a idade: '))
alistamento = 18
anoAtual = datetime.now().year

print('Você nasceu em {}'.format(anoAtual - idade))

if idade > 18:
    print('Seu período de alistamento já passou')
    print('Já se passaram {} ano(s) desde sua oportunidade de alistamento!'.format(idade - alistamento))
elif idade == 18:
    print('Você está na idade de se alistar')
else:
    print('Você ainda não tem idade para se alistar!')
    print('Faltam {} ano(s) para seu alistamento'.format(alistamento - idade))