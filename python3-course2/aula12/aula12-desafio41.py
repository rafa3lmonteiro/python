# A Confederação Nacional de Natação precisa de um programa que leia o ano de
# nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

ano = int(input('Entre com o ano de nascimento: '))
calc_idade = 2019 - ano

if calc_idade <= 9:
    print('Até 9 anos: MIRIM - idade: {}'.format(calc_idade))
elif calc_idade <= 14 and calc_idade > 9:
    print('Até 14 anos: INFANTIL - idade: {}'.format(calc_idade))
elif calc_idade <= 19 and calc_idade > 14:
    print('Até 19 anos: JUNIOR - idade: {}'.format(calc_idade))
elif calc_idade <= 25 and calc_idade > 19:
    print('Até 25 anos: SENIOR - idade: {}'.format(calc_idade))
else:
    print('Acima de 25 anos: MASTER - idade: {}'.format(calc_idade))
