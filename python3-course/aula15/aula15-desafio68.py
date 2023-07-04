# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando
# o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
import time
vitorias = 0
numeropc = randint(0, 10)
escolha_pc = 'x'
calculo = 0

while True:
    print('#'*40)
    print('\033[1;32;40m###       Jogo de Par ou Impar       ###\033[m')
    print('#'*40)
    escolha_minha = str(input('Escreva sua Escolha Par ou Impar ? [Par / Impar]: \n')).upper()

    numero = int(input('Agora escolha um numero: '))

    print(f'Voce escolheu: {escolha_minha} e o numero: {numero}')
    time.sleep(2)
    if escolha_minha == 'PAR':
        escolha_pc = 'IMPAR'
    else:
        escolha_pc = 'PAR'
        print(f'Então o Computador vai ser {escolha_pc}')
    print('\n ** PAR !! IMPAR !! ** ')
    print('computador esta pensando em um numero... ')
    time.sleep(4)
    print(f'O computador escolheu numero ( {numeropc} )')
    calculo = numero + numeropc
    print(f'Voce escolheu {escolha_minha} e {numero} - O Computador {escolha_pc} e {numeropc} - {numero}+{numeropc} = {calculo}')
    time.sleep(3)
    resto = calculo % 2
    vencedor = 'x'
    if resto == 0:
        print(f'\n*****     {calculo} é PAR !    *****')
        vencedor = 'PAR'
    else:
        print(f'\n*****     {calculo} é IMPAR !     *****')
        vencedor = 'IMPAR'
    if escolha_minha == vencedor:
        print('Parabens vc \033[1;32;46m GANHOU \033[m do Computador  =D ')
        vitorias += 1
        print(f'Voce já ganhou do computador {vitorias} Vezes !')
        time.sleep(2)
        print('\n Vamos jogar mais até voce perder ?? ')
    else:
        print('\nVoce \033[1;31;47m PERDEU :( \033[m - Game Over !')
        print(f'Voce ganhou do computador: {vitorias} vezes')
        break

#print('\033[1;32;40m Olá Mundo !\033[m')