import time

#Iniciar váriaveis
lista_num = []
valor = 0

#Loop para obter dados
for i in range(0, 5):
    #print(len(lista_num))
    valor = 0
    valor = int(input('Digite um valor: '))
    lista_num.append(valor)
    #print(len(lista_num))

print(f'Original: {lista_num}')

#Copiar a lista
tupla_lista_num = lista_num[:]
max1 = max(tupla_lista_num)
min1 = min(tupla_lista_num)

#Remover o maior da lista e inserir ele na ultima posição
lista_num.remove(max1)
lista_num.insert(5, max1)

#print(f'Ajustado o maior: {lista_num}')

#Remover o menor da lista e inserir ele na ultima 1° posição
lista_num.remove(min1)
lista_num.insert(0, min1)

#print(f'Ajustado o menor: {lista_num}')

#2° Copia
lista_num_c = lista_num[:]
lista_num_c.remove(max1)
lista_num_c.remove(min1)

#print(f'Lista pos filtro: {lista_num_c}')

#Trabalhando no restante
max2 = max(lista_num_c)
min2 = min(lista_num_c)

#Remover o maior da lista e inserir ele na ultima posição da lista 2

lista_num_c.remove(max2)
lista_num_c.insert(2, max2) # Posição 2, pois a lista 2 só tem 3 posições

#Remover o menor da lista e inserir ele na 1° posição da lista 2
lista_num_c.remove(min2)
lista_num_c.insert(0, min2)

#print(f'Lista pos ajuste: {lista_num_c}')

#Finalizar - unir dados

lista_num_f = (lista_num[0], lista_num_c[0], lista_num_c[1], lista_num_c[2], lista_num[4])

print(f'A lista final organizada é: {lista_num_f}')


'''
#Metodo Guana

lista = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]: #Se ele estiver no final da lista ou no inicio, OBS: o ultimo sempre vai ser oque formos adicionando
        lista.append(n)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(lista): #Enquanto a pocisão for menor que o tamanho da lista, controle
            if n <= lista[pos]:
                lista.insert(pos, n) #Usar o insert
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'Osa valores digitados em ordem foram {lista}')
            



'''





