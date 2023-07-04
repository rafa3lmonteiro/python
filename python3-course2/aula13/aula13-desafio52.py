# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um numero: '))
tot = 0

for c in range(1, num +1):
    if num % c == 0:
        print('\033[33m', end='')  # aqui esotu mandando pintar de amarelo o que for divisivel pelo contador c
        tot += 1
    else:
        print('\033[31m', end='') # aqui estou mandando pintar de vermelho se nao for divisivel pelo contador c
    print('{} '.format(c), end='')
print('\n \033[m O numero {} foi divisivel {} vezes'.format(num, tot))

if tot == 2:    # se o total de divisao pelo contador for = 2, é um numero primo
    print('O numero {} é um numero PRIMO !!'.format(num))
else:
    print('O numero {} NÀO é um numero primo'.format(num))
