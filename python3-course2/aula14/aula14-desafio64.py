# Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
cont = -1
total = 0
num = 0
while num != 999:
    total += num
    num = int(input('Digite um numero inteiro qualquer, ou 999 para sair: '))
    print(num)
    cont += 1
print('-'*30)
print('Foram digitados: {} Numeros'.format(cont))
print('A Soma de todos os numeros digitados foi: {}'.format(total))