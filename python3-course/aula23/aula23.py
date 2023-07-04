# Curso Python #23 - Tratamento de Erros e Exceções

# Primeiros exemplos da Aula

#try:
#    a = int(input('Numerador: '))
#    b = int(input('Denominador: '))
#    r = a / b
#except Exception as teste:
#    print(f'Problema encontrado foi {teste.__class__}')
#else:
#    print(f'O Resultado é {r:.1f}')
#finally:
#    print('Volte sempre ! Muito Obrigado !')

#---------------------------------------------------------------

#Segunda parte

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que vc digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir um número por Zero !')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')

else:
    print(f'O Resultado é {r:.1f}')
finally:
    print('Volte sempre ! Muito Obrigado !')

