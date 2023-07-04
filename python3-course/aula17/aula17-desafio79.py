# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final,
# serão exibidos todos os valores únicos digitados, em ordem crescente.
# https://youtu.be/LkAzRnc_GPk

lista = []

while True:
    entrada = int(input('Digite um valor aqui: '))
    if entrada in lista:
        print('Esse valor ja existe na lista ! digite outro valor !')
    else:
        lista.append(entrada)
    resp = str(input('Deseja digitar mais algum valor ? [S/N]: ')).upper()
    if resp == 'N':
        break
print(f'Nossa lista contem os valores em ordem crescente: {sorted(lista)}')
