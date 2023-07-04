# Desenvolva um programa que leia o comprimento de três retas e
# diga ao usuário se elas podem ou não formar um triângulo.

print('~#~' * 20)
print('Analisado de Triangulos')
print('~#~' * 20)
r1 = float(input('Digite o tamanho do primeiro Segmento: '))
r2 = float(input('Digite o tamanho do segundo Segmento: '))
r3 = float(input('Digite o tamanho do terceiro Segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os Segmentos acima podem formar um Triangulo !')
else:
    print('Os Segmentos acima não podem formar um triangulo !')

