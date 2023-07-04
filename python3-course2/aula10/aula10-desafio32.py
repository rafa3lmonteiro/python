# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
# Função : Bissexto - Um ano é bissexto se ele for divisível por 400 ou se ele
#         for divisível por 4 e não por 100.
# Bissexto:  1980, 1984, 1988, 1992, 1996 e 2000.
#          1900 não foi bissexto, mas 1600 foi
from datetime import date
ano = int(input('Digite o ano: '))

if ano == 0:    # Bonus, se colocar o ano 0, vai mostrar o ano atual do meu computador
    ano = date.today().year

if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print('{} É um ano Bissexto !'.format(ano))
else:
    print('{} Não é Bissexto'.format(ano))

