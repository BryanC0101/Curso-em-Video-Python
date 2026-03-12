#Utilizando funções para fazer cálculo de área
def area(largura, comprimento):
    calculo = largura * comprimento
    print(f'A área do terreno de {largura}m x {comprimento}m é de {calculo}m²')

largura = float(input('Largura: (m) '))
comprimento = float(input('Comprimento: (m) '))

print('Calculando a área de um terreno')
print('-=-'*30)
area(largura, comprimento)