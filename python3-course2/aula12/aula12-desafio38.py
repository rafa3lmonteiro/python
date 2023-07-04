# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

if num1 > num2:
    print('O numero 1: {} é maior que o numero 2: {}'.format(num1, num2))
elif num2 > num1:
    print('O numero 2: {} é maior que o numero 1: {}'.format(num2, num1))
else:
    print('Os numero 1: {} e numero 2: {} são iguais'.format(num1, num2))










