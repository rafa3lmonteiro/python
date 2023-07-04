# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos
# B) Quantos homens foram cadastrados
# C) Quantas mulheres tem menos de 20 anos
contidade = 0
conthomem = 0
novinhas = 0

print('## Programa de cadastro de Usuarios ##')
while True:
    sexo = str(input('Digite o sexo [M/F]: ')).upper()
    while sexo != 'M' and sexo != 'F':
        print('Digitou errado, digite novamente mula !')
        sexo = str(input('Digite o sexo [M/F]: ')).upper()
    if sexo == 'M':
        conthomem +=1

    idade = int(input('Digite sua idade: '))
    if idade >= 18:
        contidade +=1
    if sexo == 'F' and idade <= 20:
        novinhas +=1
    continua = str(input('Deseja continuar ? [S/N]: ')).upper()
    if continua == 'N':
        break
print('finalizando programa...')
print('-'*30)
print('#### Resultados ####')
print(f'Numero de maiores de 18 anos: {contidade}')
print(f'Numero de Homens: {conthomem}')
print(f'Quantidade de mulheres menores de 20 anos: {novinhas}')