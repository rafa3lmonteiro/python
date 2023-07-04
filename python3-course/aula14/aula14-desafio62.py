# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer
# mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro = int(input('Digite o primeiro elemento: '))
razao = int(input('Entre com a Razão da PA: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(primeiro), end='')
        primeiro += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais vc quer mostrar ?: '))
print('Fim da Progressão... com {} termos mostrados'.format(total))

