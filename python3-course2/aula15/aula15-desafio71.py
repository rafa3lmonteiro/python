# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início,
# pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
# cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cedulas de 50, 20, 10 e 1
cont50 = 0
cont20 = 0
cont10 = 0
cont1 = 0
print('### Caixa 24h - Banco Bonus Hora ###')

saque = int(input('Qual valor deseja sacar ?: '))
print(f'Voce deseja sacar: {saque} Reais\n')
while saque != 0:
    while saque / 50 >= 1:
        saque = saque - 50
        cont50 +=1
    while saque / 20 >= 1:
        saque = saque - 20
        cont20 +=1
    while saque / 10 >= 1:
        saque = saque - 10
        cont10 +=1
    while saque / 1 >= 1:
        saque = saque - 1
        cont1 +=1
if cont50 >=1:
    print(f'Seu saque sera em {cont50} notas de 50 Reais')
if cont20 >=1:
    print(f'Seu saque sera em {cont20} notas de 20 Reais')
if cont10 >=1:
    print(f'Seu saque sera em {cont10} notas de 10 Reais')
if cont1 >=1:
    print(f'Seu saque sera em {cont1} notas de 1 Real')

