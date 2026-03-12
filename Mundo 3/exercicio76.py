#Organizando de forma tabular preços e produtos com tuplas

listagem = ('Pão', 1.00, 'Salgadinho', 6.99, 'Café' , 22.99, 'Arroz', 24.99, 'Feijão', 16.99, 'Carne', 35.99, 'Leite', 30.99, 'Farinha', 12.99, 'Refrigerante', 9.99)

nums = ()
strings = ()

print('---------------------------------------------')
print('LISTAGEM DE PREÇOS')
print('---------------------------------------------')

for c in range(0, 18):
    if isinstance(listagem[c], float):
        nums += (listagem[c],)


for y in range(0, 18):
    if isinstance(listagem[y], str):
        strings += (listagem[y],)


for p in range(0, 8):
    print(f"{strings[p]:.<30}R$ {nums[p]:>7.2f}")


print('---------------------------------------------')