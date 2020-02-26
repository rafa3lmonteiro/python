# Curso Python #19 - Dicionários

pessoas = {'nome': 'Rafael', 'sexo': 'M', 'idade': 30}
print(f'{pessoas["nome"]}')

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

print(pessoas.keys())       # aqui eu mostro as chaves do dicionario pessoas
print(pessoas.values())     # aqui eu mostro os valores do dicionario pessoas
print(pessoas.items())      # aqui eu mostro os itens do dicionario pessoas
print()
for k in pessoas.keys():   # Para K sendo pessoas.keys mostre o K
    print(k)
print()

for v in pessoas.values():  # Para V sendo pessoas.values mostre o V
    print(v)
print()

pessoas['nome'] = 'Monteiro'    # aqui eu alterei o valor do nome
pessoas['peso'] = 85.4          # aqui eu adicionei um item no dicionario, no final dele
del pessoas['sexo']             # aqui eu deletei o item sexo do dicionario

for k, v in pessoas.items():
    print(f'{k} = {v}')

