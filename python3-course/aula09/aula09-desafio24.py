# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome da cidade: '))
print('Cidade: {}'.format(cidade))

print('Existe SANTO nome desta cidade ?:','Santo' in cidade)