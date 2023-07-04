#Curso Python #15 - Interrompendo repetições while

n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}')  # Na versão nova do Python podemos utilizar as F Strings simplicando o format desta forma


