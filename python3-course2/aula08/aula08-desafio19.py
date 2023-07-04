#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice

aluno1 = str(input('Digite o nome do 1 aluno: '))
aluno2 = str(input('Digite o nome do 2 aluno: '))
aluno3 = str(input('Digite o nome do 3 aluno: '))
aluno4 = str(input('Digite o nome do 4 aluno: '))

string_list = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(string_list)

print ('\n O aluno escolhido aleatoriamente para apagar a lousa eh o {}'.format(escolhido))
