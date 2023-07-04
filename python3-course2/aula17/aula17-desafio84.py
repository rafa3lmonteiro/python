# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

temporaria = []
principal = []
mai = men = 0
while True:
    temporaria.append(str(input('Nome: ')))
    temporaria.append(float(input('Peso: ')))
    if len(principal) == 0:
        mai = men = temporaria[1]
    else:
        if temporaria[1] > mai:
            mai = temporaria[1]
        if temporaria[1] < men:
            men = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('=-'*30)
print(f'Foram cadastradas {len(principal)} Pessoas')
print(f'O maior peso foi o de {mai}KG. Peso de ', end='')
for p in principal:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi o de {men}KG. Peso de ', end='')
for p in principal:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()

