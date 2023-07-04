#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

aluno1 = str(input('Digite o nome do 1 aluno: '))
aluno2 = str(input('Digite o nome do 2 aluno: '))
aluno3 = str(input('Digite o nome do 3 aluno: '))
aluno4 = str(input('Digite o nome do 4 aluno: '))

string_list = [aluno1, aluno2, aluno3, aluno4]
print ('Lista original', string_list)

random.shuffle(string_list)
print ('Lista sorteada',string_list)
print ('\n Sorteio ordem de aprensentacao dos trabalhos: \n 1- {}\n 2- {}\n 3- {}\n 4- {}\n '.format(string_list[0], string_list[1], string_list[2], string_list[3]))