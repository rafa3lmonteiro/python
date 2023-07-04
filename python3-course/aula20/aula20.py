# Curso Python #20 - Funções (Parte 1)


def lin():
    print('-' * 30)

#lin()
#print('    SISTEMA DE ALUNOS     ')
#lin()


def titulo(texto):
    print('-' * 30)
    print(texto)
    print('-' * 30)


titulo('     CURSO EM VIDEO     ')


def soma(a, b):
    s = a + b
    print(s)


soma(4, 5)
soma(8, 9)
soma(2, 1)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A+B = {s}')


#Programa principal
soma(7, 2)
soma(b=4, a=5)  # Nesta caso eu especifico a ordem, podendo muda-la
