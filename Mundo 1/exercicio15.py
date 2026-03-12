dias = int(input('Quantos dias usados? '))
km = int(input('Quantos km foram rodados? '))

calc = (km * 0.15) + (dias * 60)

print('Você terá que pagar R${}'.format(calc))