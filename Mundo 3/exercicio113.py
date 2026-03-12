import requests
try:
    resposta = requests.get('https://pudim.com.br/')
    if resposta.status_code == 200:
        print('\033[32mO site está acessível!\033[m')
    else:
        print('\033[31mO site está inacessível, tente em outro momento!\033[m')
except:
    print('\033[34mO site está inacessível por erro de conexão, tente em outro momento!\033[m')