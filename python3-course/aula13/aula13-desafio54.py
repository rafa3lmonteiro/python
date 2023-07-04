# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date   # importanto a função Date da biblioteca Datetime para nos informar o ano atual
ano_atual = date.today().year  # atribuindo o ano atual na variavel ano_atual
totmaior = 0
totmenor = 0

for pessoas in range(1, 8):     # para pessoas sendo de 1 a 7
    nasc = int(input('Em que ano a {}" pessoa nasceu: '.format(pessoas)))
    idade = ano_atual - nasc
    if idade >= 21:
        totmaior += 1       # incrementando +1 no numero total de totmaior usando o += 1
    else:
        totmenor += 1       # mesma coisa para o menor
print('Ao total tivemos {} pessoas maiores de idade'.format(totmaior))
print('E tambem tivemos {} pessoas menores de idade'.format(totmenor))

