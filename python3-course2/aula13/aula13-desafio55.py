# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 100
for pess in range(1, 6):
    peso = int(input('Digite o {}" peso em kg : '.format(pess)))

    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('=~'*15)
print('O maior peso é: {}'.format(maior))
print('E o menor peso é: {}'.format(menor))