#Feito com a droga do chatgpt, não consegui fazer esse de forma alguma

# Tupla com palavras
palavras = ("Python", "Programacao", "Computador", "Aluno")

# Tupla com vogais
vogais = ("a", "e", "i", "o", "u")

for c in palavras:
    print(f"\nNa palavra '{c}' temos: ", end="")
    for y in c.lower():
        if y in vogais:
            print(y, end=" ")