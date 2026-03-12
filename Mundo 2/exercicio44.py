#Pagamento de produto

pago = float(input('Digite o valor do produto: '))

aVista = pago - (pago * 0.10)
aVistaCard = pago - (pago * 0.05)
cardJuros = pago + (pago * 0.20)

print('Você prefere pagar como?')
print('À VISTA:                    DIGITE: 1')
print('À VISTA NO CARTÃO:          DIGITE: 2')
print('2x NO CARTÃO:               DIGITE: 3')
print('3x OU MAIS NO CARTÃO:       DIGITE: 4')

escolha = int(input('Digite sua escolha: '))

if escolha == 1:
    print(aVista)
elif escolha == 2:
    print(aVistaCard)
elif escolha == 3:
    print(pago)
elif escolha == 4:
    print(cardJuros)
else:
    print('Por favor, digite os números de 1 a 4 para a realização da compra')




