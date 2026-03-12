#Reforçando os conhecimentos do exercicio 35


reta1 = float(input('Digite a medida da primeira reta em centimetros: '))
reta2 = float(input('Digite a medida da segunda reta em centimetros: '))
reta3 = float(input('Digite a medida da terceira reta em centimetros: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('Sim, as retas formam um triângulo!')   
    if reta1 / reta2 == 1 and reta1 / reta3 == 1:
     print('O triângulo que será formado será EQUILÁTERO')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('O triângulo que será formado será ISÓSCELES')
    elif reta1 != reta2 and reta1 != reta3 and reta2 != reta3:
     print('O triângulo que será formado será ESCALENO')
else:
    print('Não, essas retas não podem formar um triângulo')

