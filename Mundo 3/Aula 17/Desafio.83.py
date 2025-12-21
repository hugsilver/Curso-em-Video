import time
from sys import exec_prefix

'''
open = close = 0

expresse = (str(input('Digite a expressão: ')))

for c in expresse:
    if c == '(':
        open += 1
    elif c == ')':
        close += 1


if open > close or open < close:
    print('As expressões não são iguais!!!')
else:
    print('As expressões são iguais!!!')
'''


#Método guanabara

exec_prefix = str(input('Digite a expressão: '))
pilha = []

for simb in exec_prefix:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está válida.')
else:
    print('Sua expressão está errada.')