# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que
# se encontram no intervalo de 1 até 500.
print('mostrando numeros multiplos de 3 de 1 ate 500:')
for x in range(1, 501):
    if x % 3 == 0:
        print(x)
print('FIM')