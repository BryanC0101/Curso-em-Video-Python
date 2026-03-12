#Lendo dados de produtos

escolha = 0
total = 0
maisDeMil = 0
produtoLowPrice = 0
produtoNomePrice = ''

while True:
    nomeProduto = str(input('Informe o nome do produto: ')).strip().upper()
    precoProduto = float(input('Qual o preço do produto: R$'))

    """if produtoLowPrice == precoProduto:
        produtoNomePrice = print('\033[33mHá dois ou mais produtos com valores iguais\033[m')"""

    

    if produtoLowPrice > precoProduto:
        produtoNomePrice = nomeProduto
        produtoLowPrice = precoProduto
    elif produtoLowPrice == 0:
        produtoNomePrice = nomeProduto
        produtoLowPrice = precoProduto


    


    if precoProduto > 1000:
        maisDeMil += 1 
    
    total += precoProduto

    escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if escolha == 'S':
        continue
    elif escolha == 'N':
        break
    else:
        escolha = str(input('\033[33mEscolha uma opção válida: [S/N] \033[m')).strip().upper()
    
        

print('='*40)
print(f'O gasto total foi de: R$\033[31m{total:.2f}\033[m')
print(f'\033[31m{maisDeMil}\033[m produtos custaram mais de R$1000')
print(f'O produto mais barato foi de: R$\033[31m{produtoLowPrice}\033[m sendo ele o/a: \033[31m{produtoNomePrice}\033[m')
print('='*40)

