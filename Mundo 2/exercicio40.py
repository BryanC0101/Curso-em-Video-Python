#Calculando média do aluno

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5.0 and media >= 0.0:
    print('Sua média foi de {}'.format(media))
    print('Você foi reprovado!')
    print('Estude mais')
elif media >= 5.0 and media <= 6.9:
    print('Sua média foi de {}'.format(media))
    print('Você ficará na recuperação!')
    print('Terá bastante tempo para estudar!')
elif media >= 7.0 and media <= 10.0:
    print('Sua média foi de {}'.format(media))
    print('Parabéns, você foi aprovado!')
else:
    print('Para de mentir! É feio')