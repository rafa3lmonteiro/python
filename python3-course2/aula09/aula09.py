frase = "          Curso em Video Python           "

#print(frase.upper().count('O'))
#print(frase.replace('Python', 'android'))
#print(frase.strip())
#print('Curso' in frase)
#print(frase.lower().find('python'))

frase_separada = frase.split()
print('separando a frase',frase_separada)
print('quero a terceira palavra da frase -> ',frase_separada[2])

frase_junta = '-'.join(frase_separada).upper()
print(frase_junta)