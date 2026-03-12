#Fazendo linhas acompanharem o tamanho do texto

def escreva(texto):
    print('~'*(len(texto) + 4))
    print(f"{texto:^{len(texto) + 4}}")
    print('~'*(len(texto) + 4))

digitando = str(input('Escreva aqui: '))
escreva(digitando)