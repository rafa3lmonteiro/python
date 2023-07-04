# Faça um programa que leia o nome completo de uma pessoa e:
# - mostrando em seguida o primeiro e o último nome separadamente.

n = str(input('Digite seu nome completo: ')).strip()

#acima fazendo um strip no nome para eliminar espaços no inicio e fim da frase
#abaixo fazendo um split no nome para dividir em blocos cada nome

nome = n.split()

# imprimindo o nome na bloco 0, primeiro nome
print('Seu Primeiro nome é: {}'.format(nome[0]))

# imprimindo o nome usando o len para calcular quantos blocos existem -1, imprimindo o ultimo bloco
print('Seu ultimo nome é: {}'.format(nome[len(nome)-1]))


