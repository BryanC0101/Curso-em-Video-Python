#Boletim escolar
from time import sleep
lista = []
lista_nomes = []
lista_notas = []
lista.append(lista_nomes)
lista.append(lista_notas)
escolha = 's'
pesquisa = 0
while escolha == 's':
    nome = str(input('Informe o nome do aluno: '))
    nota1 = float(input('Digite a \033[31mprimeira\033[m nota: '))
    nota2 = float(input('Digite a \033[36msegunda\033[m nota: '))
    lista_nomes.append(nome)
    lista_notas.append(nota1)
    lista_notas.append(nota2)
    escolha = str(input('Quer continuar? [S/N]')).strip().lower()
    if escolha == 's':
        continue
    elif escolha == 'n':
        break
    else:
        while escolha != 's' and escolha != 'n':
            escolha = str(input('Tente novamente, quer continuar? [S/N] ')).strip().lower()



print('-=-'*20)
print('Nº Nome', end='')
print('Média'.center(20))
print('-'*25)
for c in range(len(lista_nomes)):
    print(f'{c} {lista_nomes[c]} {((lista_notas[c*2] + lista_notas[c*2 + 1]) / 2):.2f}')



print('-'*25)
print('-=-'*20)



while pesquisa != 999:
    pesquisa = int(input('Mostrar notas de qual aluno? [999 intemrrompe] '))
    if pesquisa == 999:
        break
    else:
        print(f'As notas de {lista_nomes[pesquisa]} são: ', end='')
        print(lista_notas[pesquisa*2], end=', ')
        print(lista_notas[pesquisa*2 + 1])
print('---FINALIZANDO---')
sleep(1)
print('Volte sempre!')
#[ [nome[nota1, nota2]], [nome[nota1, nota2]] ]
