#Fazendo novamente o exercício 51, só que agora com While

p1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Informe a razão da PA: '))
termos = 0
escolha = 0

while termos != 10 and termos < 11:
    termos += 1
    an = p1 + (termos - 1) * r
    print ('{}'.format(an), end='')
    print(' ⮕ ' if termos != 10 else '', end='')


