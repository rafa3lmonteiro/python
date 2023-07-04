# Desenvolva um programa que leia seis números inteiros e mostre
# a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

num1 = int(input('Numero 1: ')) # Recebendo os 6 numeros de entrada
num2 = int(input('Numero 2: '))
num3 = int(input('Numero 3: '))
num4 = int(input('Numero 4: '))
num5 = int(input('Numero 5: '))
num6 = int(input('Numero 6: '))

soma = 0    # definindo a variavel de soma, começando zerada

for x in range(num1, num6+1): # para o renge dos inputs de num1 a num6 +1 (porque senao nao pega o ultimo)
    if x % 2 == 0:              # so quero os numeros pares, com resto de divisão por 2 = a zero
        print('numero par: {}'.format(x))
        soma = soma + x             # sempre que for par, soma-se este numero a variavel soma
print('Total da soma de numeros pares é = {}'.format(soma))
