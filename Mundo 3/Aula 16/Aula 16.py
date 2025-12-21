
lanche = ('Hamburg' , 'Suco' , 'Pizza' , 'Pudim')
print(lanche[1]) #Na hora de referenciar usar o []
print(lanche[1:3])
print(lanche[:2]) #Ham e Suco
print(lanche[-2:])
print(lanche[-3:])
print(lanche)

for comida in lanche:
    print(f'Eu vou comer {comida}')

print('Comi muito')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

#Enumerate traz dado quanto posição

#sorted - Ordenada - Em ordem

print(sorted(lanche))
# Sorted retorna em [] ou sejá transforma uma tupla em lista


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
#del(c)
print(c) #União das tuplas
print(sorted(c))
print(len(c))

print(c.count(4)) #Quantas vezes aparecer certo valor na tupla

#index

print(c.index(5, 1)) # Qual posição está o valor


#Vetor - Dados de um mesmo tipo

#Uma coisa que modifica a tupla - Del





'''
#Tupla são imutaveis
Pode-se inicar uma váriavel com () - Tupla, {} - Lista  [] - Dicionario 

'''