#Progressão aritimética

p1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

for c in range(1, 11):
    an = p1 + (c-1) * razao
    print(an, end=' → ')