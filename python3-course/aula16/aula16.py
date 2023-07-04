# Curso Python #16 - Tuplas
# Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python.
# As tuplas são variáveis compostas e imutáveis que permitem armazenar vários
# valores em uma mesma estrutura, acessíveis por chaves individuais.

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)

print(lanche[-2])   #vai me mostrar o segundo ultimo item do indice
print(lanche[1:3])  #vai me mostrar o elemento 1 e 3 do indice
print(lanche[2:])   #vai me mostrar do fim até os 2 ultimos elementos
print(lanche[:2])   #vai me mostrar do inicio até o segundo elemento
print(lanche[-3:])  #vai me mostrar do suco até o final, terceiro ultimo ate o fim

for comida in lanche:
    print(f'Eu vou comer {comida}')

print('-'*30)
#mesmo resultado porem usando o Len
#aqui vou usar o len para contar o cumprimento da minha tupla e assim mostrar ela
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

print('\n Comi pra caramba\n')
# aqui eu vou mostrar a comida e sua posição no indice de 2 formas
# com enumerate e com o len (mesmo resultado porem utilizando formas diferentes)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('-'*30)

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

print('-'*30,'\n')
print(lanche)
print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(f'tupla a = {a}')
print(f'tupla b = {b}')
print(f'soma a + b = {c}')
print(f'a tupla c tem: {len(c)} elementos ')
print(f'nesta tupla aparece o numero 5:  {c.count(5)} Vezes')  #quantas vezes esta aparecendo o numero 5
print(f'Em que posição de indice esta o numero 8 ?:  {c.index(8)} ')
print(f'Onde esta o numero 5 a partir da posição 2 ?:  {c.index(5, 2)}') #chamamos de Deslocamento

#Nas tuplas nós podemos colocar diferentes tipos de dados, ex:

pessoa = ('Rafael', 33, 'M', 83.40)
print(pessoa)

del(pessoa) #apaguei essa tupla, serve para qualquer outra variavel tbm
