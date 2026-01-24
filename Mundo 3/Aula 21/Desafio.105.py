
import statistics

def notas(a=0 , b=0, c=0, d=0, sit = 0):
    """
    Docstring para notas
    -> Função para analisar notas e situações de vários alunos
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """

    lista = list()
    if a >= 0:
        lista.append(a)
    if b >= 0:
        lista.append(b)
    if c >= 0:
        lista.append(c)
    if d >= 0:
        lista.append(d)

    med = statistics.mean(lista)

    
    contador = len(lista)
    dicionario = dict()
    dicionario = {'Quantidade': contador, 'Maximo': max(lista), 'Minimo': min(lista), 'Media': med}

    if sit == True:
        if med >= 6:
            dicionario['Situ'] = 'BOA'
        else:
            dicionario['Situ'] = 'RUIM'

    return dicionario 

#Programa Principal
resp = notas(8, 2, 3, 9, sit=True)
print(resp)




