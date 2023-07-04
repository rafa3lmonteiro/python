# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

# Entrando com o numero para a fatoração
n1 = int(input('Entre com o numero a ser fatorado: '))

print('Sera fatorado o numero: {}'.format(n1))
result = 1
for x in range(1, n1+1):
    result = result * x
print('Fatorando de 1 até {}'.format(n1))
print('-'*40)
print('O resultado da fatoração é: {}'.format(result))

