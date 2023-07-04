# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
media = (nota1 + nota2)/2
print('media = {:.2f}'.format(media))

if media < 5:
    print('Média abaixo de 5.0: {} REPROVADO'.format(media))
elif media <= 6.9 and media >= 5:
    print('Média entre 5.0 e 6.9: {} RECUPERAÇÃO'.format(media))
else:
    print('Média 7.0 ou superior: {} APROVADO'.format(media))