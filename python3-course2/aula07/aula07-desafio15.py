
#Entrada de dados referente a km percorridos e dias usando o carro

qtd_km = int(input('Qual foi a quantidade de Km percorridos pelo carro alugado:  '))
qtd_dias = int(input('Entre com a quantidade de dias pelos o carro foi alugado:  '))
valor_dia = 60
valor_km = 0.15
total_dia = qtd_dias * valor_dia
total_km = qtd_km * valor_km

#Calculo de valor a pagar e saida dos dados
print('Voce rodou {} KMs e usou o carro por {} dias, valor a pagar {}'.format(qtd_km, qtd_dias, total_dia + total_km ))
