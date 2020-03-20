# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros
# opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do
# jogador, mesmo que algum dado não tenha sido informado corretamente.


def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

# Programa principal
n = str(input('Nome do Jogador: '))
g = str(input('Numero de gols: '))  #vou ler Gol como string que ele diexa ficar vazio

if g.isnumeric():   # Aqui, Se o meu G é numerico eu torno ele (int)
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)