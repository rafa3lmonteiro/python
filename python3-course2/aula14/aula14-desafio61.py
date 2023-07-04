# Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro = int(input('Digite o primeiro elemento: '))
razao = int(input('Entre com a Razão da PA: '))

c = 1

while c <= 10:
    print('{} -> '.format(primeiro), end='')
    primeiro += razao
    c += 1
print('FIM')