#Curso Python #17 - Listas (Parte 2)

# Variaveis compostas

dados = list()
dados.append('Pedro')
dados.append(25)
dados.append('Maria')
dados.append(19)
dados.append('João')
dados.append(32)
print(dados[:]) #imprimir todo o fatiamento

#pessoas.append(dados[:])
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]

print(pessoas[1])

print(pessoas[0][0])