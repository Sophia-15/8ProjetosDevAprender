import random
from time import sleep


min = 1
max = 6
q = str(input('Você deseja jogar o dado? [s/n] ')).upper()

def valor():
    valor = random.randint(min, max)
    sleep(0.5)
    print(f'O valor do dado é {valor}')

try: 
    if q == 'SIM' or q == 'S':
        valor()
        q = str(input('Você deseja jogar o dado? [s/n] ')).upper()

    elif q == 'NÃO' or q == 'N' or q == 'NAO':
        print('Obrigado por jogar! Tenha um bom dia!')
    
    else:
        print('Por favor, digite sim ou não.')
        q = str(input('Você deseja jogar o dado? [s/n] ')).upper()
        sleep(0.5)
        valor()
except:
    print('Ocorreu um erro')

