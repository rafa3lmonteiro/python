# Curso Python #014 - Estrutura de repetição while

for x in range(1, 10):
    print(x)
print('FIM')

print('-='*20)
# Mesmo resultado porem usando estruturas diferentes

c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar ? [S/N] ')).upper()
print('Fim')
