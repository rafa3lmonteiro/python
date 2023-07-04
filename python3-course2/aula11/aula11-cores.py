# Aula 11 - cores no terminal

#Neste caso eu abro o codigo de cores, coloco o codigo do estilo; texto; back e fecho depois do texto
print('\033[1;31;40m Olá Mundo !\033[m')

#Neste exemplo eu utilizo o codigo de cores com o .format, onde o codigo de cor entra nos {} e fecha tbm
nome = 'Rafael'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

# Neste exemplo abaixo eu crio variaveis para as cores, desta forma eu não preciso ficar digitando codigo, somente as cores definidas em variaveis
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[1;7;30m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))