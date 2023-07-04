# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes
print('~#~' * 20)
print('Analise de Triangulos')
print('~#~' * 20)
r1 = float(input('Digite o tamanho do primeiro Segmento: '))
r2 = float(input('Digite o tamanho do segundo Segmento: '))
r3 = float(input('Digite o tamanho do terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os Segmentos acima podem formar um Triangulo: ', end='') # este end junta este print com o print resultante do if
    if r1 == r2 == r3:  # o Python me permite fazer comparação de 3 valores ao memso tempo
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1:  # Neste caso eu estou testando se os 3 lados são diferentes um do outro, no final do r3
        print('ESCALENO')       # eu preciso saber se ele é diferente do r1 tbm, porque ele poderia ser igual e o teste ficar falho
    else:
        print('ISÓCELES')
else:
    print('Os Segmentos acima não podem formar um triangulo !')