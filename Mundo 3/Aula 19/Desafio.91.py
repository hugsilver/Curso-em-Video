
'''
from random import randint

dado = dict()
dado_ord = list()
i = 1


#Gerar dicionario com valores rand
dado['jogador1'] = randint(1, 6)
dado['jogador2'] = randint(1, 6)
dado['jogador3'] = randint(1, 6)
dado['jogador4'] = randint(1, 6)
print(dado)

#Mostar dicionario
for v, k in dado.items():
    print(f'O {v} tirou {k}')

#Ordenando pelo sorted de valores
print('\n')
dado_ord = dict(sorted(dado.items(), key=lambda item: item[1], reverse=True))


Esse método está pegando um dicionário, ordenando ele pelos valores e devolvendo um novo dicionário ordenado
sorted(..., key=lambda item: item[1], reverse=True)
sorted(...) ordena essa lista.
item é cada tupla (chave, valor).
A função key=lambda item: item[1] diz:
“Use o segundo elemento da tupla (ou seja, o valor do dicionário) como critério de ordenação”.
Reverse=True significa ordenar do maior para o menor.

print(dado_ord)

#Ranking dos jogadores
for j, l in dado_ord.items():
    print(f'O {i}° lugar: {j} com {l}')
    i +=1
'''

#Metodo Guana

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1' : randint(1, 6), 'jogador2' : randint(1, 6), 'jogador3' : randint(1, 6), 'jogador4' : randint(1, 6)}

print(jogo)
print('Valores sorteados:')
ranking = list()
for v, k in jogo.items():
    print(f' - {v} tirou {k} no dado')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # Arg 0 - Ordem de chave, se for 1 - Ordem de valor
print(ranking)

for v, k in enumerate(ranking):
    print(f'{v+1}° lugar {k[0]} com {k[1]}')
    sleep(1)