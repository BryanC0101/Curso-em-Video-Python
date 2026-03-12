#Projeto mais ambicioso até agora do curso
#Fazer o Python se conectar a um bloco de texto e personalizá-lo com nomes e idades
#Isso tudo savando-os mesmo que se encerre o programa

def limpar_nomes():
    import os
    pasta = os.path.dirname(__file__)
    arquivo_txt = os.path.join(pasta, 'arquivo.txt')
    with open(arquivo_txt, "w") as file:
        pass

def escrever_txt(str, int):
    import os
    pasta = os.path.dirname(__file__)
    arquivo_txt = os.path.join(pasta, 'arquivo.txt')
    with open(arquivo_txt, "a") as file:
        file.write(f'{str:<30}{int} anos\n')

def ler_txt():
    import os
    pasta = os.path.dirname(__file__)
    arquivo_txt = os.path.join(pasta, 'arquivo.txt')
    with open(arquivo_txt, "r") as file:
        conteudo = file.read()
    print(conteudo)

def ler_nome(nome):
    name = input(nome)
    while True:
        if name.isnumeric():
            name = input('\033[31mDigite um nome válido: \033[m')
        else:
            break
    return name

def ler_idade(idade):
    age = input(idade)
    while True:
        if not age.isnumeric():
            age = input('\033[31mDigite uma idade válido: \033[m')
        else:
            break
    return age



while True:
    print('~'*40)
    print('MENU PRINCIPAL'.center(40))
    print('~'*40)
    print('\033[33m1\033[m - \033[34mVer pessoas cadastradas\033[m')
    print('\033[33m2\033[m - \033[34mCadastrar novas pessoas\033[m')
    print('\033[33m3\033[m - \033[34mLimpar cadastros\033[m')
    print('\033[33m4\033[m - \033[34mSair do sistema\033[m')
    escolha = input('\033[32mSua opção: \033[m')

    if not escolha.isnumeric():
        print('\033[31mDigite um número válido\033[m')
        continue

    escolha = int(escolha)

    if escolha < 1 or escolha > 4:
        print('\033[31mOpção inválida\033[m')
        continue

    if escolha == 1:
        ler_txt()
    elif escolha == 2:
        nome = ler_nome('Digite um nome: ')
        idade = ler_idade('Digite a idade: ')
        escrever_txt(nome, idade)
    elif escolha == 3:
        limpar_nomes()
    elif escolha == 4:
        break
print('Volte sempre!')