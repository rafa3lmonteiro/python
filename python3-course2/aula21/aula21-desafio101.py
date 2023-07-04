# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano
# de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL
# e OBRIGATÓRIO nas eleições.
# menor de 16 não vota, entre 16 e 18 o voto é OPCIONAL, entre 18 e 65 Voto Obrigatorio, acima de 65 anos é opcional


def voto(nasc):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - nasc
    if idade < 16:
        return f'Com {idade} anos: Voce NÃO VOTA ainda !'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Seu voto é OPCIONAL !'
    else:
        return f'Com {idade} anos: Obrigatorio votar no Bolsonaro !'


print('-' * 35)
resp = int(input('Em que ano vc nasceu ?  '))
print(voto(resp))
