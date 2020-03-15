# Curso Python #21 - Funções (Parte 2)

#print(input.__doc__)
#help(input)

# Fazendo uma DocString

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Funcão criado por Rafael Monteiro em 13/03/2020
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')

help(contador)

# Vendo Escopo de Variaveis

def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
funcao()
print(f'N1 fora vale {n1}')

#-------------
print()

def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A Fora vale {a}')
