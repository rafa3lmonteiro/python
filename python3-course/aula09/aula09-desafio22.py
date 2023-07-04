# Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras
# maiúsculas e minúsculas - Quantas letras ao - todo sem considerar espaços -
# Quantas letras tem o primeiro nome.

nome = str(input('Digite o seu nome completo: '))

print('Nome:',nome)
print('Nome Maiusculo: {}'.format(nome.upper()))
print('Nome minusculo: {}'.format(nome.lower()))

separa = nome.split()
junta = ''.join(separa)
print('Numero de letras sem considerar espaços: {}'.format(len(junta)))

print('Numero letras do primeiro nome: {}'.format(len(separa[0])))