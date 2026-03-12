vel = int(input('Qual foi a velocidade do veículo? '))


#bloco do cálculo
valorMulta = 0
if vel > 80:
 valorMulta = (vel - 80) * 7 


#bloco dos prints
if vel <= 80:
    print('Tudo normal por aqui, tenha um bom dia!')
else:
    print('Você foi multado, e sua multa é de R${}'.format(valorMulta))