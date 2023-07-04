# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares
# digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista = []
listapar = []
listaimpar = []
while True:
    num = (int(input('Digite um numero: ')))
    lista.append(num)
    resp = str(input('Deseja continuar ? [S/N]: '))
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)
    if resp in 'Nn':
        break
print('-='*30)
print(f'Nossa lista COMPLETA contem: {lista}')
print(f'Nossa lista PAR contem: {listapar}')
print(f'Nossa lista IMPAR contem: {listaimpar}')