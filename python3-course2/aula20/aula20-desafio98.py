# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
# fim e passo. Seu programa tem que realizar três contagens através da função criada:
#
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep


def contador(i, f, p):

    if p < 0:
        p *= -1  # se o passo for negativo eu faco * -1 para mudar o sinal dele para Positivo
    if p == 0:
        p = 1

    print('=-' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1.5)
    if i < f:   # é o caso normal
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)  # na versao nova do Python, ele faz um cache no laco, com a opcao Flush=True ele desabilita isso, para mostrar o sleep trabalhando
            sleep(0.5)
            cont += p
        print('- FIM')
    else:       # sendo o inicio menor que o fim faca isso: ex 10 ate 0 de 2 em 2
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('- FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print('=-' *20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio:  '))
fim = int(input('Fim:     '))
pas = int(input('Passo:   '))
contador(ini, fim, pas)