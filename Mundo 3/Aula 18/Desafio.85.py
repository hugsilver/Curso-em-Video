from bisect import insort_right

#Acredito que não foi do jeito que o Guana queria, mas foi

'''
value = 0
numbers = list()
nump = list()
numi = list()

for n in range(0, 7):

    value = int(input('Digite um valor: '))

    if value % 2 == 0:
        nump.append(value) #Value no index 0


    elif value % 2 != 0:
        numi.append(value) #Value no index 0

numbers.append(sorted(nump))
numbers.append(sorted(numi))

print(numbers)
'''

#Método Guanabara

num = [[], []] #Declaração de duas listas dentro de uma outra lista

valor = 0

for i in range(1, 8):
    valor = int(input(f'Digite o {i} valor: '))
    if valor % 2 == 0:
        num[0].append(valor) #Value no index 0


    elif valor % 2 != 0:
        num[1].append(valor)  # Value no index 1

print('-='*30)
num[0].sort()
num[1].sort()
print(f'Todos os valores: {num}')
print(f'Todos os valores pares listados foram: {num[0]}')
print(f'Todos os valores impares listados foram: {num[1]}')

