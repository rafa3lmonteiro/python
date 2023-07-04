# Pacote Dado


def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()  # substitua todas virgulas por ponto e tire os espaços em branco
        if entrada.isalpha() or entrada == '': # Se a entrada for alphanumerica ou a entrada sem os espaços for vazio
            print(f'\033[0;31m ERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)
