# Curso Python #012 - Condições Aninhadas

nome = str(input('Qual é o seu nome?: '))
if nome == 'Rafael':
    print("Que nome bonito !")
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem comum no Brasil..')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal {}'.format(nome))
print('Tenha uma bom dia {}'.format(nome))
