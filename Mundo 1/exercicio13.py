#Calcular salário da pessoa

salario = int(input('Digite o salário: '))
acrecimo = 0.15
calc = (salario * acrecimo) + salario
print('O salário reajustado é agora: {}'.format(calc))