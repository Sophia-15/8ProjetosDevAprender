import random
import random


min = 1
max = 100

chute = int(input('Chute um valor de 1 a 100: '))
valor = random.randint(min, max)

while chute != valor:
    if chute < valor:
        print('Chute mais alto!')
        chute = int(input('Chute um valor de 1 a 100: '))
    elif chute > valor:
        print('Chute mais baixo!')
        chute = int(input('Chute um valor de 1 a 100: '))
    if chute == valor:
        print(f'Parabéns! Seu chute era {chute}, e o valor era {valor}.')