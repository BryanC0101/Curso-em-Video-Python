#As retas formam um triângulo?

reta1 = float(input('Digite a medida da primeira reta em centimetros: '))
reta2 = float(input('Digite a medida da segunda reta em centimetros: '))
reta3 = float(input('Digite a medida da terceira reta em centimetros: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('Sim, as retas formam um triângulo!')
else:
    print('Não, essas retas não podem formar um triângulo')