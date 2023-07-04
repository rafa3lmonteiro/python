# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
cont = -1
total = 0
num = 0
media = 0
maior = 0
menor = 9999
while num != 999:
    total += num

    if num > maior:
        maior = num
    num = int(input('Digite um numero inteiro qualquer, ou 999 para sair: '))
    print(num)
    cont += 1

    if num < menor:
        menor = num

media = total / cont
print('-'*30)
print('Foram digitados: {} Numeros'.format(cont))
print('A Soma de todos os numeros digitados foi: {}'.format(total))
print('A Média dos numeros digitados é: {}'.format(media))
print('O Maior numero digitado foi: {}'.format(maior))
print('O Menor numero digitado foi: {}'.format(menor))
