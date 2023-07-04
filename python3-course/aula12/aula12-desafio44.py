# Elabore um programa que calcule o valor a ser pago por um produto, considerando:
# O seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros
print('#--'*15)
preco = float(input('Qual é o preço do produto ?: '))
print('-'*25)
# Calculo das formas de pagamento
dinheiro_cheque = preco - (preco * 0.10)
avista_cartao = preco - (preco * 0.05)
cartao2x = preco
cartao3x = preco + (preco * 0.20)
print('#  Condições de Pagamento: ','\n','-'*25)
print('Dinheiro ou Cheque   - desconto de 10%: {:.2f}'.format(dinheiro_cheque))
print('A Vista no Cartão    - desconto de 5%: {:.2f}'.format(avista_cartao))
print('Cartão em 2x         - preço normal: {:.2f}'.format(cartao2x))
print('Cartão em 3x         - Juros de 20%: {:.2f}'.format(avista_cartao))


