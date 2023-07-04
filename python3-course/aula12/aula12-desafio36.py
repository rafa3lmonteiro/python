# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa, Pergunte:
# - O valor da casa,
# - O salário do comprador e
# - Em quantos anos ele vai pagar.
# OBS: A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Entre com o valor da casa que voce vai Financiar R$: '))
prazo_pagamento = int(input('Em quantos anos vc quer pagar: ')) * 12
valor_parcela = valor_casa / prazo_pagamento
salario = float(input('Entre o valor do seu salario atual R$: '))
margem_salario = salario * 0.30
#print("vc vai pagar seu financiamento no prazo de {} meses".format(prazo_pagamento))
#print('sua parcela mensal nao pode passar de {:.2f}'.format(margem_salario))

if valor_parcela > margem_salario:
    print('\nFinanciamento NEGADO, o valor de sua parcela mensal R${:.2f} ultrapassa os 30% da sua margem que é R${}'.format(valor_parcela, margem_salario))
else:
    print('\nFinanciamento APROVADO ! \nValor total do Bem: R${:.2f} \nNumero de parcelas: {} Meses \nValor da Parcela: R${:.2f}'.format(valor_casa, prazo_pagamento, valor_parcela))