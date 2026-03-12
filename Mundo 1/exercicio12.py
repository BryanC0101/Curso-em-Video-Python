#Desconto do preço

preco = float(input("Qual o preço: "))

desc = 0.05
calc = preco * (1 - desc)

print('Seu valor com 5% de desconto é {}'.format(calc))