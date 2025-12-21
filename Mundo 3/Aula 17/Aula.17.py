
'''
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2) #Na posição 2 inserir o valor 2
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')

#num.remove(2) #Vai tirar somente o 1° elemento
#num.pop() #Retira o ultimo
#num.pop(5) #Remove o indice 5
print(num)
print(f'Essa lista tem {len(num)} elementos')

'''

'''
valores = []

valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f' Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista.')
'''

'''
valores = list()

for cont in range(0, 5):
    valores.append(int(input('Digite o valor: ')))

for c, v in enumerate(valores):
    print(f' Na posição {c} encontrei o valor {v}')
print('Chegguei ao final da lista.')
'''

a = [2, 3, 4, 7]
b = a # Ligação - Cuidado
b = a[:] # Copia de A dentro de B
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')