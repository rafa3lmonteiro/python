# continuando as anotacões
# Retorno de Funcões


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)

print(f'Meus calculos deram {r1}, {r2} e {r3}.')

# ---------------------------------


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados Fatoriais são {f1}, {f2} e {f3}')

# ---------------------------------
print()


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um numero para saber se ele é Par: '))
print(par(num))

# ---------------------------------
print()


def par2(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um numero para saber se ele é Par: '))
if par2(num):
    print('É Par! ')
else:
    print('Não é Par !')

