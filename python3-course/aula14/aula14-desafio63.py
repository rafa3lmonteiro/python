# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e
# mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

n = int(input('Entre com um numero para ver essa quantidade em Fibonacci:  '))

a, b = 0, 1
while a < n:
        print(a, end=' ')
        a, b = b, a + b
        print()
