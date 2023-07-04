# Escreva um programa que:
# - Pergunte o salário de um funcionário e calcule o valor do seu aumento.
# - Para salários superiores a R$1250,00, calcule um aumento de 10%.
# - Para os inferiores ou iguais, o aumento é de 15%.

salario = int(input('Qual é o seu salario ?:  '))

calculo1 = salario + (salario * 0.10)
calculo2 = salario + (salario * 0.15)

if salario >= 1250:
    print('Seu salario hoje é de R${}, com aumento de 10% passara a receber R${}'.format(salario, calculo1))
else:
    print("Seu salario hoje é de R${}, com aumento de 15% passara a receber R${}".format(salario, calculo2))
