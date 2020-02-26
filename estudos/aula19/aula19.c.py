estado = dict()
brasil = list()
for c in range(0, 3):       # Realizando a entrada de dados com for e range
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())        # importante lembra, que fatiamento não funciona para dicionarios
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}')   # Vou mostrar cada chave e valor de cada estado
    print()

for x in brasil:
    for v in x.values():
        print(v, end=' ')
    print()


