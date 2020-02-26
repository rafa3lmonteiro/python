# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista
# composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
# de cada aluno individualmente.
lista = list()
alunos = list()

while True:
    nome = str(input('Digite o nome: '))
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))
    lista.append(nome)
    lista.append(nota1)
    lista.append(nota2)
    alunos.append(lista[:])
    lista.clear()
    resp = str(input('Desenja cadastrar mais alnos ? [S/N] '))
    if resp in 'Nn':
        break
print('-='* 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{(a[1]+a[2])/2:>8.1f}')
while True:
    notaaluno = str(input('Quer mostrar a nota de qual aluno ?  (exit para sair): '))
    for n in alunos:
        if notaaluno in n[0]:
            print(f'O {n[0]} teve as Nota 1 - [{n[1]}] e Nota 2 - [{n[2]}]')
    if notaaluno == 'exit':
        break
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
