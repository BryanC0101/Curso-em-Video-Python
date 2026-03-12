#Gerando números aleatórios e colocando na tupla
import random
numeros = tuple(random.randint(1, 10) for _ in range(5))
print(numeros)
print(f'O maior número gerado na tupla é: {max(numeros)}')
print(f'O menor número gerado na tulpa é: {min(numeros)}')