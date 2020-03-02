# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
# pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoa = dict()
lista = list()
somaidade = 0
listamulheres = list()
listaacimamedia = list()

while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: '))
    pessoa['idade'] = int(input('Idade: '))
    somaidade += pessoa['idade']
    lista.append(pessoa.copy())

    if pessoa['sexo'] in 'Ff':
        listamulheres.append(pessoa.copy())
    pessoa.clear()
    resp = str(input('deseja cadastrar mais alguma pessoa ? [S/N]: '))
    if resp in 'Nn':
        break
mediaidade = somaidade / len(lista)
print('-='*30)
print(f'Foram cadastrados: {len(lista)} pessoas')
print(f'Media de idade: {mediaidade:.2f} anos')
print(f'Lista com a mulheres: ')
for m in listamulheres:
    print(f'   - {m["nome"]} com {m["idade"]} anos')
print()
print('Pessoas com a idade maior que a Media de idade: ')
for i in lista:
    if i['idade'] > mediaidade:
        print(f'   - {i["nome"]} com {i["idade"]} anos')
print()