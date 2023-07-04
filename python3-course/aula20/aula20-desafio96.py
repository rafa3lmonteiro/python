# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um
# terreno retangular (largura e comprimento) e mostre a área do terreno.


def lin():
    print('-=' *20)


def area(lar, comp):
    total = lar * comp
    print(f'A area total do terreno é {total:.2f}')


print('\n- Digite os dados da area - \n')
l = float(input('Largura: '))
c = float(input('Comprimento: '))

print()
lin()
area(l, c)
lin()