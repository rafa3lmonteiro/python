# Curso Python #20 - Funções (Parte 1)


def lin():
    print('-' * 30)


def contador(* num):
    for valor in num:
       print(f'{valor} ', end='')
    print(' - FIM')
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros')


lin()
contador(2, 1, 7)
lin()
contador(8, 0)
lin()
contador(4, 4, 7, 6, 8)

lin()


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2  # Multipicla a posicão por 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)
print(f'Minha lista valores dobrada é {valores}')

lin()

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)