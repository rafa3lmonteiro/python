# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
# resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o
# maior número no dado.
from time import sleep
from random import randint
from operator import itemgetter
jogo = {'jogador01': 0, 'jogador02': 0, 'jogador03': 0, 'jogador04': 0}
ranking = list()

for x in jogo.keys():
    dado = randint(1, 6)
    jogo[x] = dado
    sleep(.7)
    print(f'{x} tirou {jogo[x]} no dado ')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='* 30)
print('  == Ranking dos Jogadores ==  ')
for i, v in enumerate(ranking):
    print(f'   {i+1}o. lugar: {v[0]} com {v[1]}')
    sleep(.7)