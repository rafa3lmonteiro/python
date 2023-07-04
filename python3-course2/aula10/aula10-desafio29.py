# Escreva um programa que leia a velocidade de um carro.
# - Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# - A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Entre com a velocidade do carro: '))
multa = (velocidade - 80) * 7

if velocidade > 80:      #estou utilizando condicional simples porque nao preciso de else neste caso, ficou mais simples
    print('Vc passou da velocidade permitida, vai tomar multa ! \nVoce tomou uma multa de : R${}'.format(multa))

print('Vc esta dentro do limite permitido, siga bem caminhoneiro !')
