# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e
# cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

lista = []

for x in range(0, 5):
    n = int(input('Digite um valor: '))
    if x == 0 or n > lista[-1]: # Se for o primeiro valor (==0) ou N é maior que o ultimo elemento da lista, faça o append (ultima posição):
        lista.append(n)
        print(f'{n} Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram: {lista}')
