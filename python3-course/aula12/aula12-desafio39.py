# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# - se ele ainda vai se alistar ao serviço militar,
# - se é a hora exata de se alistar ou
# - se já passou do tempo do alistamento.
# - Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
ano = int(input('Jovem em qual ano você nasceu ? : '))
idade = 2019 - ano
print('Voce tem {} anos de idade'.format(idade))

if idade < 18:
    print('Voce ainda vai precisar se alistar para o Servico Militar')
    print('Falta {} anos para voce se alistar'.format(18 - idade))
elif idade == 18:
    print('Esta no momento exato para voce se Alistar para o Servico Militar !')
elif idade > 18:
    print('Já passou do momento para voce se Alistar para o Servico Militar, esta atrasado, paga 10 !')
    print('Voce esta atrasado em {} anos'.format(idade - 18))