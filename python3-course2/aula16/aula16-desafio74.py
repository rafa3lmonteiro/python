# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
# mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os valores sorteados foram: ', end='')
for x in numeros:
    print(f'{x} ', end='')

print(f'\nO maior numero sorteado foi: {max(numeros)}')
print(f'O menor valor sorteado foi: {min(numeros)}')