# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
# em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
import random    # codigo desafio 28
import time

num = random.randint(0, 5) # aqui o computador vai "escolher" um numero entre 0 e 5
print('~#~' * 15)
num_usuario = int(input('Tente descobrir um numero entre 0 e 5 que o computador escolheu: '))
print('O Usuario escolheu: ',num_usuario)
print('~#~' * 20)
print('PROCESSANDO...')
time.sleep(1)
contador = 0
while num_usuario != num:
    print('Voce errou, tente novamente !')
    num_usuario = int(input('Digite um numero entre 0 e 5: '))
    contador += 1
print('Parabens vc acertou ! o computador escolheu o numero {}'.format(num))
print('Voce usou {} tentativas ate acertar'.format(contador))