#Sabendo média, min e max de números inteiros digitados
escolha = 'S'
n = 0
quantidade_num = 0
soma_para_media = 0
maior = 0
valores = []


while escolha == 'S':
    n = int(input('Informe um número: '))
    valores.append(n)
    if maior < n:
        maior = n

    quantidade_num += 1
    soma_para_media += n
    escolha = str(input('Deseja continuar? [S/N]')).upper()
media = soma_para_media / quantidade_num
print('A média dos números foi de: {:.2f}'.format(media))
print('O maior número foi: {}'.format(maior))
print('O menor número foi: {}'.format(min(valores)))
