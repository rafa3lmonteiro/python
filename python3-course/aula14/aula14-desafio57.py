# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite o sexo da Pessoa [M/F]: '))
r = 'S'
while sexo != 'M' and sexo != 'F':
    print('Valor invalido, favor digitar M para Masculino e F para Feminimo')
    sexo = str(input('Tente novamente, Sexo da Pessoa é [M/F] ?: '))
print('Pessoa do sexo - {}'.format(sexo))

