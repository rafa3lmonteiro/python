# Crie um programa que faça o computador jogar Jokenpô com você. Pedra, Papel ou Tesoura
# Este programa deve pedir para o usuario escolher entre:
# 1 - Pedra / 2 - Papel / 3 - Tesoura
# a partir da escolha do usuario o computador faz uma escolha randomica entre os 3, e ve quem ganha
from time import sleep          # importando os componetes sleep e randint dos modulos time e random
from random import randint
cores = {'limpa':'\033[m',      # criando sistemas de cores atraves de variaveis
         'verde':'\033[1;32m',
         'amarelo':'\033[1;33m',
         'vermelho':'\033[1;31m'}

itens = ('Pedra', 'Papel', 'Tesoura')   # criando a lista dos itens, onde o campo 0 é Pedra, 1 Papel e 2 Tesoura
computador = randint(0, 2)              # criando a variavel de sorteio do computador usando randint que vai sortear
                                        # os numero no range de 0 ate 2
print('-'*35)
print('Bem vindo ao Jogo de Jo Ken Pô ')
print('-'*35)
print('''Suas Opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura ''')
jogador = int(input('Qual é a sua Jogada ?  '))
if jogador != 0 and jogador != 1 and jogador != 2:  # Criando uma condição para caso o jogador digite algo diferente de 0, 1 e 2
        print('Opção Invalida !! ')
        exit(0)
print('~='* 14)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !!!')
print('O Jogador jogou: {}'.format(itens[jogador]))
print("O Computador jogou: {}".format(itens[computador]))
print('~='*14)
    # Criando a cadeia de IF dentro de if com elif e else, definindo que para cada escolha do computador teremos
    # 3 possiveis jogadas do Jogador ou uma jogada invalida
if computador == 0: # computador jogou Pedra
    if jogador == 0:
        print('{} EMPATE !{} '.format(cores['amarelo'], cores['limpa'])) # para cada inicio de cor, é preciso fechar a cor, senao pinta tudo dali pra baixo
    elif jogador == 1:
        print('{} Jogador Ganhou !{}'.format(cores['verde'], cores['limpa']))
    elif jogador == 2:
        print('{} Computador Ganhou !{}'.format(cores['vermelho'], cores['limpa']))
    else:
        print('Jogada Invalida !')

elif computador == 1: # computador jogou Papel
    if jogador == 0:
        print('{} Computador Ganhou !{}'.format(cores['vermelho'], cores['limpa']))
    elif jogador == 1:
        print('{} EMPATE !{} '.format(cores['amarelo'], cores['limpa']))
    elif jogador == 2:
        print('{} Jogador Ganhou !{}'.format(cores['verde'], cores['limpa']))
    else:
        print('Jogada Invalida !')

elif computador == 2: # computador jogou Tesoura
    if jogador == 0:
        print('{} Jogador Ganhou !{}'.format(cores['verde'], cores['limpa']))
    elif jogador == 1:
        print('{} Computador Ganhou !{}'.format(cores['vermelho'], cores['limpa']))
    elif jogador == 2:
        print('{} EMPATE !{} '.format(cores['amarelo'], cores['limpa']))
    else:
        print('Jogada Invalida !')