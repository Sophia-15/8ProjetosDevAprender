#Programa onde vai lhe decidir fazer algo para você
from random import choice


pergunta = str(input('Faça sua pergunta: '))

respostas = [
    'Hmmmm acho que não é uma boa ideia', 
    'Tu é doidé??? Faça isso não',
    'Depende, eu num vou poder ajudar nessa',
    'SIM',
    'Eu acho que a segunda opção é a melhor'
]

print(choice(respostas))