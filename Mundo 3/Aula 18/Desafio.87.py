
'''
matrix = [[1, 2, 3], [4, 5, 6] , [7, 8, 9]] #Ainda não sei como criar uma lista dentro de uma lista do berço
somap = somac = 0


for j in range(0, 3):
    for i in range(0,3):

        #print(matrix[i][j])
        value = int(input(f'Digite o valor da célula {j}x{i}: '))
        matrix[j][i] = value
        if value % 2 == 0:
            somap += value
        if (i == 2):
            somac += value

    #print(p)
    #time.sleep(1)

for p in matrix:
    print(p)

print(f'A soma dos valores pares é: {somap}')
print(f'A soma dos valores da terceira coluna é: {somac}')
print(f'O maior valor da segunda linha é: {max(matrix[1])}')
'''

#Metodo Guana

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0 ]] #Para não usar append serve declarar a estutura com valores pre-definidos

spar = mai = scol = 0



for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Digite um valor para {l}X{c}: '))

print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='' ) #Formatado com 5 caracteres centralizados
        if matrix[l][c] % 2 == 0:
            spar += matrix[l][c]

    print()
print('-='*30)
print(f'A soma dos valores pares é {spar}')

for l in range(0, 3):
    scol += matrix[l][c]
print(f'A soma dos valores da terceira coluna é {scol}')

for c in range(0, 3):
    if c == 0:
        mai = matrix[1][c]
    elif matrix[1][c] % 2 == 0:
        mai = matrix[1][c]
print(f'O maior valor da segunda linha é {mai}')