#Conversor de Celcius para Fahrenheit

temp = float(input('Informe a temperadura em °C: '))

conv = temp * (9/5) + 32

print('A temperatura {}°C corresponde a {}°F!'.format(temp, conv))