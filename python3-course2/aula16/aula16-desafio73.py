# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
# de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times. (Fatiamento)
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética. (Sorted)
# d) Em que posição está o time da Chapecoense.

tabela = ('Flamengo','Santos','Palmeiras','Grêmio','Athletico-PR','São Paulo','Internacional',
          'Corinthians','Fortaleza','Goias','Bahia','Vasco','Atlético-MG','Fluminense','Botafogo',
          'Ceara','Cruzeiro','CSA','Chapecoense','Avai')

print('-='*30)
print(f'Lista de times do Brasileiro 2019: {tabela}')
print('-='*30)
print(f'Os 5 Primeiros são: {tabela[:5]}')
print('-='*30)
print(f'Os 4 Últimos colocados são: {tabela[-4:]}')
print('-='*30)
print(f'Times em ordem alfabética {sorted(tabela)}')
print('-='*30)
print(f'O Chapecoense esta na {tabela.index("Chapecoense")+1}* posição')