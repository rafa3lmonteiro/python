# Escreva um programa que faça o computador "pensar" em:
# - um número inteiro entre 0 e 5 e
# - peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# - O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
import time

num = random.randint(0, 5) # aqui o computador vai "escolher" um numero entre 0 e 5

print('~#~' * 20)
num_usuario = int(input('Senhor Usuario, tente descobrir um numero entre 0 e 5 que o computador escolheu: '))
print('O Usuario escolheu: ',num_usuario)
print('~#~' * 20)
print('PROCESSANDO...')
time.sleep(3)

if num_usuario == num:
    print('Parabéns !!! Você acertou, o numero {} que o computador escolheu'.format(num))
else:
    print('Voce errou, o numero que o computador escolheu foi o numero {}'.format(num))
