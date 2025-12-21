from operator import index

lista_num = []
num = 0

for i in range (0, 5):
     num = int(input('Digite um valor: '))
     lista_num.append(num)

print(lista_num)


for indice , valor in enumerate(lista_num):

    if valor == max(lista_num):
       print(f'O maior elemento está no indeci {indice} com valor {valor}')

    elif valor == min(lista_num):
        print(f'O menor elemento está no indeci {indice} com valor {valor}')






