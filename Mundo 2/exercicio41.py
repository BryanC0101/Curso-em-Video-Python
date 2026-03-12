#Classificar atleta
from datetime import datetime

anoNascimento = int(input('Digite o ano de nascimento da/do atleta: '))

anoAtual = datetime.now().year
idade = anoAtual - anoNascimento

if idade <= 9:
    print('Você entra na categoria MIRIM')
elif idade > 9 and idade <= 14:
    print('Você entra na categoria INFANTIL')
elif idade > 14 and idade <= 19:
    print('Você entra na categoria JUNIOR')
elif idade == 20:
    print('Você entra na categoria SÊNIOR')
elif idade > 20:
    print('Você entra na categoria MASTER')
