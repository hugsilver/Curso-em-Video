
import time
from bisect import insort_right

'''
matrix = [[1, 2, 3], [4, 5, 6] , [7, 8, 9]]

for j in range(0, 3):
    for i in range(0,3):

        #print(matrix[i][j])
        value = int(input(f'Digite o valor da célula {j}x{i}: '))
        matrix[i][j] = value
    #print(p)
    #time.sleep(1)

for p in matrix:
    print(p)
'''

#Método Guanabara

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0 ]] #Para não usar append serve declarar a estutura com valores pre-definidos

for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Digite um valor para {l}X{c}: '))

print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='' ) #Formatado com 5 caracteres centralizados
    print()

