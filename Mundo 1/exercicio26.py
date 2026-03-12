n = input('Digite uma frase: ').lower().strip()

print ('A letra "a" aparece: {}'.format(n.count('a')))
print ('A primeira posiçao de "a" é: {}'.format(n.find('a')))
print ('A última posiçao de "a" é: {}'.format(n.rfind('a')))
