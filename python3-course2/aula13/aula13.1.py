# Continuação aula 13

num = int(input('Entre com um numero para ver sua contagem: '))

for c in range(1, num+1):
    print(c)
print('\nFIM')

##################

inicio = int(input('Digite o primeiro numero, inicio: '))
fim = int(input('Digite o fim da sua sequencia: '))
passo = int(input('Digite qual o passo para percorrer esse sequencia:'))

for x in range(inicio, fim+1, passo):
    print(x)
print('\nFIM')