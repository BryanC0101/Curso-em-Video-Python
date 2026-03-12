#Dar aumento de salário

salario = float(input('Digite o salário do funcionário: '))

if salario > 1250.00:
   aumentoSalario = salario * (10 /100)
   novoSalario = salario + aumentoSalario
   print('Seu aumento salarial foi de R${:.2f}, e agora seu salário é de R${:.2f}'.format(aumentoSalario, novoSalario))
elif salario <= 1250.00:
   aumentoSalario = salario * (15 /100)
   novoSalario = salario + aumentoSalario
   print('Seu aumento salarial foi de R${:.2f}, e agora seu salário é de R${:.2f}'.format(aumentoSalario, novoSalario))