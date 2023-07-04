# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
# se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
totalgasto = 0
maisde1000 = 0
nomemaisbarato = 'x'
valormaisbarato = 999999999
produto = 'x'
valor = '0'
print('##### Mercado Baratão Voador #####')
print('Cadastro de produtos ')
while True:
    produto = str(input('nome do produto: '))
    valor = float(input('valor R$: '))
    totalgasto += valor
    if valor < valormaisbarato:
        valormaisbarato = valor
        nomemaisbarato = produto
    if valor >= 1000:
        maisde1000 += 1
    cont = str(input('\nDeseja cadastrar mais item ? [s/n]')).upper()
    while cont != 'S' and cont != 'N':
        print('Digite novamente, S ou N')
        cont = str(input('Deseja cadastrar mais item ? [s/n]')).upper()
    if cont == 'N':
        break
print(f'\nTotal gasto na compra: {totalgasto}')
print(f'Voce comprou {maisde1000} produtos +1000 Reais !')
print(f'O produto mais barato foi o {nomemaisbarato} com o valor de {valormaisbarato} ')