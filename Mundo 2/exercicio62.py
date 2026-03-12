#Melhorando novamente o exercício 51, agora com mudança de termos pelo usuário

p1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Informe a razão da PA: '))
termos = 0
escolha = 'S'
resposta_termos = 10

while escolha == 'S':
    while termos != resposta_termos:
        termos += 1
        an = p1 + (termos - 1) * r
        print ('{}'.format(an), end=' ⮕ ')
    escolha = str(input('\nDeseja continuar? [S/N] ')).upper()
    if escolha == 'S':
        termos = resposta_termos
        resposta_termos += int(input('Digite quantos termos a mais você quer: '))
        continue
    else:
        print('Obrigado por usar o programa, volte quando necessitar!')
        break

  
        