# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
#
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
#
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.


def notas(*n, sit=False):
    """
    -> Funcão para analisar notas e situacões de varios alunos
    :param n: uma ou mais notas dos alunos (aceita varias notas)
    :param sit: valor opcional, indicando se deve ou não adicionar a situacão
    :return: dicionario com varias informacões sobre a situacão da turna.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:     # se o param sit for verdadeiro, faca:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


# Programa principal

resp = notas(5.5, 2.5, 1.5, 8.5, sit=True)
print(resp)