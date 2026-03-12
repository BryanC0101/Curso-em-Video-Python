#Analisando se uma expressão matemática está correta ou errada
lista = []
aberto = 0
fechado = 0
expressao = input('Digite sua expressão matemática: ')
lista.append(expressao)
for c in range(0, len(lista[0])):
    if '(' in lista[0][c]:
        aberto += 1
    if ')' in lista[0][c]:
        fechado += 1
if aberto == fechado:
    print('Sua expressão está \033[32mcorreta!\033[m')
else:
    print('Sua expressão está \033[31merrada!\033[m')

#se a quantidade de eparenteses for impar, está errado, se não está certo