# Exercício Python 030: Crie um programa que leia um número inteiro e
# - Mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Entre com um numero inteiro: '))

resto_divisao = num % 2  # calculando o resto da divisao, se sobrar 1 é impar, se sobrar 0 é par

if resto_divisao == 0:
    print('Este numero é par, numero {}'.format(num))
else:
    print('Este numero é impar, numero {}'.format(num))