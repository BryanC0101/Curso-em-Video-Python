#Calculando gols de jogador e se ele existe ou os gols existem com parâmetros
#Aqui não consegui identificar que precisava do isnumeric(), portanto necessitei da ajuda do
#chat-gpt para me auxiliar na tarefa

def futebol(jogador='<<desconhecido>>', gols=0):
    print(f'O jogador {jogador} fez {gols} no campeonato.')

nome_jogador = str(input('Qual o nome do jogador? '))
quantos_gols = input('Quantos gol(s) ele fez no campeonato? ')

if quantos_gols.isnumeric():
    quantos_gols = int(quantos_gols)
else:
    quantos_gols = 0

if nome_jogador:
    futebol(nome_jogador, quantos_gols)
else:
    futebol(gols=quantos_gols)