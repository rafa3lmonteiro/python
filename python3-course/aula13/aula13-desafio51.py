# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input('Digite o primeiro elemento: '))
razao = int(input('Entre com a Razão da PA: '))
n = int(input('Quantos elementos exibir na PA? : '))

ultimo = primeiro + (n-1)*razao
ultimo = ultimo + 1

for x in range(primeiro, ultimo, razao):
    print(x)
