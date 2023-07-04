# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida
print('~~#~~' * 15)
print('#    Bem vindo a Calculadora de IMC - Indice de Massa Corpórea ')
peso = int(input('\nEntre com o seu peso: '))
altura = float(input('Entre com a sua Altura: '))
imc = peso / (altura ** 2)
print('~~#~~' * 15)
if imc < 18.5:
   print('IMC abaixo de 18,5: Abaixo do Peso - Seu IMC: {:.2f}'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Entre 18,5 e 25: Peso Ideal - Seu IMC: {:.2f}'.format(imc))
elif imc >= 25 and imc < 30:
    print('Entre 25 e 30: Sobrepeso !!!- Seu IMC: {:.2f}'.format(imc))
elif imc >= 30 and imc < 40:
    print('Entre 30 e 40: OBESIDADE !!! - Seu IMC: {:.2f}'.format(imc))
elif imc >= 40:
    print('Acima de 40: OBESIDADE MORBIDA !!! - Seu IMC: {:.2f}'.format(imc))
