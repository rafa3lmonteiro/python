# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
# mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

cont = soma = 0
num = 0
while True:
    num = int(input('Digite seu numero aqui - [Ou 999 para sair]: '))
    if num == 999:
        break
    soma += num
    cont +=1
print(f'Foram digitados {cont} numeros !')
print(f'A Soma total dos numeros foi de {soma}')