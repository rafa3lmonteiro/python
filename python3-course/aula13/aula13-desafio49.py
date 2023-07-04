# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um numero de 1 a 10 pra saber sua tabuada: '))
print('~#'*15)
print('Iniciando a Tabuada do: {}'.format(num))
print('~#'*15)
for x in range(1, 11):
    print('{} x {} = {}'.format(num, x, num*x))

