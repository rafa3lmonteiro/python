# Criando uma lista vazia e adicionando valores

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

#outra forma, em que o usuario vai alimentando a lista atraves de um laço

valores2 = list()
for cont in range(0, 5):
    valores2.append(int(input(f'Digite o valor para o indice {cont}: ')))
for c2, v2 in enumerate(valores2):
    print(f'Na posição {c2} encontrei o valor {v2} !')
print('Cheguei no fim do segundo teste')

# Entendendo sobre ligação entre listas e copias de listas

a = [2, 3, 4, 7]
#b = a   # Desta forma eu crio uma ligação de uma lista com outra, tudo que eu alterar em uma espelha na outra
b = a[:] # Desta forma eu copio todos os valores de A para B, o que eu fizer em uma não afeta a outra
print(f'Lista A: {a}')
print(f'Lista B: {b}')
