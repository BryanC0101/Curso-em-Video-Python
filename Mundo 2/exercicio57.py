#Utilizando while para repetição
genero = input('Informe seu sexo [M/F] ').strip().lower()
while genero != 'm' and genero != 'f':
    genero = input('Dado inválido, informe seu sexo: ').strip().lower()
print('Sexo {} armazenado com sucesso!'.format(genero.upper()))