#Tabela do brasileirão 23/02/2026

print('=================== Classificação do Brasileirão 2026 ===================')
classificados = ('Palmeiras', 'São Paulo', 'Fluminense', 'Bahia', 'Corinthians', 'Athletico-PR', 'Bragantino', 'Chapecoense', 'Mirassol', 'Coritiba', 'Flamengo', 'Botafogo', 'Gremio', 'EC Vitória', 'Atlético-MG', 'Remo', 'Vasco da Gama', 'Santos', 'Internacional', 'Cruzeiro')

print(f'Os \033[31m5\033[m primeiros colocados são: \033[31m{classificados[0:5]}\033[m')
print(f'Os últimos \033[31m4\033[m colocados são: \033[33m{classificados[16:20]}\033[m')
print('============================================================================================================')
print(sorted(classificados))
print('============================================================================================================')
print(f'O time \033[32mChapecoense\033[m está na posição: {classificados.index('Chapecoense')}')