# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# - Calcule o preço da passagem
# - Cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = float(input('Qual é a distancia em KM para a sua viagem?: '))

if km <= 200:   # Condicional simplificado, sem necessidade do else
    print('O valor da viagem vai ser : R$ {:.2f}'.format(km * 0.50))    # {:.2f} para mostrar 2 casas decimais

print('O valor da viagem vai ser : R$ {:.2f}'.format(km * 0.45))
