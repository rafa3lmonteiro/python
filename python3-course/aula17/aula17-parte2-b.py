#Curso Python #17 - Listas (Parte 2)
#continuacão

teste = list()
teste.append('Gustavo')
teste.append('40')
galera = list()
galera.append(teste) #Nesta forma de append eu faco uma ligacão, e tudo que acontecer nesta lista flete nos futuros appends
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)

#-------------------- Fazendo o mesmo com Copia de fatiamento

teste2 = list()
teste2.append('Gustavo')
teste2.append('40')
galera2 = list()
galera2.append(teste2[:]) # Nesta maneira eu realizo uma COPIA de fateamento e sigo sem ligacão
teste2[0] = 'Maria'
teste2[1] = 22
galera2.append(teste2[:])
print(galera2)

#---------------

galera3 = [['João', 10], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera3)
print(galera3[2][1])

for p in galera3:
    print(f'{p[0]} tem {p[1]} anos de idade ')

#---------------

galera4 = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(str(input('Idade: ')))
    galera4.append(dado[:]) # Neste caso como eu estou fazendo uma copia, quando eu fizer o clear abaixo, eu não perco esta informacão no galera4
    dado.clear()
print(galera4)

for p in galera4:
    if p[1] >= "21":
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores de idade e {totmen} menos de idade')

