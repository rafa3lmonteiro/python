# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
n1 = int(input('Digite o 1* Numero: '))
n2 = int(input('Digite o 2* Numero: '))
resultado = 0
print('''Escolha uma das operações abaixo: 
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa ''')
oper = int(input('\nEscolha o numero do Operador: '))
while oper == 1:
    resultado = n1 + n2
    print('Voce estolheu somar: {} + {} = {}'.format(n1, n2, resultado))
    exit(0)
while oper == 2:
    resultado = n1 * n2
    print('Voce estolheu multiplicar: {} * {} = {}'.format(n1, n2, resultado))
    exit(0)
while oper == 3:
    if n1 > n2:
        print('{} é maior que {}'.format(n1, n2))
    else:
        print('{} é maior que {}'.format(n2, n1))
    exit(0)

while oper == 5:
    print('Saindo do programa...')
    exit(0)
