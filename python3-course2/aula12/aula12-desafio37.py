# Escreva um programa em Python que leia um número inteiro qualquer e peça:
# - Para o usuário escolher qual será a base de conversão:
# - 1 para binário,
# - 2 para octal e
# - 3 para hexadecimal.
num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das base para coversão:
[ 1 ] Converter para Binario 
[ 2 ] Converter para Octal
[ 3 ] Converter para Hexadecimal ''')
opcao = int(input('Sua Opção: '))
if opcao == 1:
    print('{} convertido em Binario fica {}'.format(num, bin(num)[2:])) #o Python ja tem a funcao bin(num) por padrao para conversao de numeros binarios
elif opcao == 2:                                                        # no final estamos fatiando a string para mostrar do 2 pra frente
    print('{} convertido para Octal fica {}'.format(num, oct(num)[2:])) # porque ao converter par bin, oct ou hex, o python usa os 2 primeiros campos
elif opcao == 3:                                                        # para identificar o numero, 0b (binario) 0o (octal) e 0x (hexadecimal) nao queremos esses 2 campos
    print('{} convertido em Hexadecimal fica {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida, tente novamente ! ')
