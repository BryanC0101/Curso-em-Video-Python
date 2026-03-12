def leiaDinheiro(num):
    lendo = (input(num)).strip().replace(',', '.')
    if not lendo.isnumeric():
        while not lendo.replace('.', '').isnumeric():
            print((f'\033[31mERRO! Digite "{lendo}" não é um número válido.\033[m'))
            lendo = input(num).strip().replace(',', '.')
    return float(lendo)
