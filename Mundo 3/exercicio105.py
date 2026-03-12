#Usando função e dicionário para pegar notas de alunos e saber suas situações
def notas(*num, situacao=False):
    """
    Função para analisar notas e situação de vários alunos
    num = notas cadastradas dos alunos
    situacao = (valor opcional) atual situação do conjunto de alunos

    return: dicionário com várias as informações necessárias para a avaliação do grupo cadastrado
    """

    ficha = {}
    soma = 0
    for c in num:
        soma += c
    media = soma / len(num)

    ficha["total"] = len(num)
    ficha["maior"] = max(num)
    ficha["menor"] = min(num)
    ficha["media"] = media

    if situacao:
        if media >= 7:
            ficha["situacao"] = 'BOA'
        elif media < 7 and media >= 6:
            ficha["situacao"] = 'RAZOÁVEL'
        elif media < 6:
            ficha["situacao"] = 'RUIM' 

    print(ficha)
help(notas)

resp = notas(3.5, 2, 6.5, 2, 7, 4, situacao=True)