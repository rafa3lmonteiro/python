#Curso Python #17 - Listas (Parte 1)

# Alterando o valor de um campo
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)   # acrescentando um indice ao final com o valor 7
#num.sort()     # ordenando minha lista
num.sort(reverse=True)  # ordenando a lista de tras pra frente
num.insert(2, 2)  # estou inserindo o valor 0 no indice 2, vai entrar entre o 5 e 3
num.remove(2)   # ele vai remover a ocorrencia do primeiro numero 2, nao vai remover todos os 2
if 5 in num:
    num.remove(5)
else:
    print('Não encontrei o numero 5')
#num.pop()   # vou remover o ultimo item numero 1
#num.pop(2)  # vou remover o indice 2, que é o numero 0 recentemente add
print(num)
print(f'Esta lista tem {len(num)} elementos.')
