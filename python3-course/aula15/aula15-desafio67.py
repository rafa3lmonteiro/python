# Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

num = 0
cont = 1

while True:
        num = int(input('De qual numero vc deseja saber a tabuada ? : '))
        print('#'*30)

        if num < 0:
                print('## Encerrando programa ao digitar numero Negativo ##')
                break

        print(f'--- Tabuada do {num} ---')
        while cont <= 10:
                print('{} x {} = {}'.format(cont, num, cont*num))
                cont +=1
        cont = 1
