
'''

t = 0
jogog = list()

n = int(input('Quantos jogos você deseja gerar: '))
jogos = [[0, 0, 0, 0, 0, 0]]*n  # Lista dentro de uma lista, n é o indice da quantidades de listas que sera gerada na lista jogos
#print(jogos)

#Criando lista de 6 numeros de forma randomica
for y in range (0, n):

    for i in range (0, 6):
        jogog.append(random.randint(1, 60))
        #time.sleep(0.5)
        #print(jogog)

#Validação, se o número já existir, ele vai substituir
    for j in jogog: # Até o 4 já que vou somar +1 no proximo, se for até 5 ele foge do range
        #print(jogog)
        t = jogog.count(j)
        #print(t)
        #time.sleep(0.5)
        if t > 1:
            jogog.remove(j) #Removendo eu posso inserir qualquer outro com o método append
            jogog.append(random.randint(1, 60))
            #time.sleep(0.5)

    #Add lista criada e ordenada no lista de jogos
    jogos[y] = sorted(jogog[:])
    jogog.clear() #Limpando para não gerar lixo ou sobre dados

for q in jogos:
    print(q)
'''

#Mètodo Guana

from time import sleep
from random import randint
lista = list()
jogos = list()
cont = 0

print('_'*30)
print('    JOGOS DA MEGA SENA    ')
print('_'*30)

quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1

while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break

    lista.sort() #Método pega - Ou seja adere ao objeto
    jogos.append(lista[:]) #Fazer uma copia da lista
    lista.clear() #Limpar a lista
    tot += 1
print('-='*3, f'SORTEANDO {quant} JOGOS', '-='*3)
for i, v in enumerate(jogos):
    print(f'Jogo {i+1}: {v}')
    sleep(1)

print('-='*5, '<BOA SORTE>', '-=*5')

#print(f'Os números sorteados foram {jogos}')





