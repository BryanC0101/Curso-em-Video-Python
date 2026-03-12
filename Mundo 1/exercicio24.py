#Começa ou não com "Santo" no início

cidade = str(input("Digite o nome de sua cidade: "))
splitcid = cidade.title().strip().split()

print(splitcid[0] == 'Santo')
