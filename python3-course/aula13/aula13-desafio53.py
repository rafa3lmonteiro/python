# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.
# Palindromo é quando uma frase invertida é igual a ela mesmo anter de ser invertida
# exemplo a sacada da casa = a sacada da casa , outro ex: ovo = ovo

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print('Voce digitou a frase {}'.format(palavras))
print('usando o Join: {}'.format(junto))
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALINDROMO')
else:
    print('Esta frase nao é um Palindromo')

# Podemos simplificar o codigo usando Fatiamento, retirando
# o For e usando uma variavel - inverso = junto{::-1]