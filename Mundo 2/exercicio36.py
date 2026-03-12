#Aprovador de empréstimo bancário

valorCasa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite seu salário: R$'))
anosPagar = int(input('Por quantos anos deseja pagar: '))

mensalidade = valorCasa / (anosPagar * 12)


if mensalidade > (salario - salario * 0.70):
    print('Sua mensalidade é de {:.2f} excede 30% de seu salário'.format(mensalidade))
    print('Portanto o empréstimo é inviável!')
else:
    print('PARABÉNS o empréstimo foi aprovado.')
    print('A mensalidade será de {:.2f}'.format(mensalidade))