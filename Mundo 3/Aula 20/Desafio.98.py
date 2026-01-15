"""
from time import sleep 

i = f = p = m = 0

def conc():
    print('Contagem Crescente:')
    
    for j in range(0,11):
        print(j, end=' ')
        sleep(0.1)
        
def cond():
    print('\nContagem Decrescente:')
    for j in range(10, -1, -2):
        print(j, end=' ')
        sleep(0.1)


def concusto(i, f, p, m):

    if m == 0:
        for k in range(i, f, p):
            print(k, end=' ')
        sleep(0.1)
    else:
        for k in range(f, i, -p):
            print(k, end=' ')
        sleep(0.1)


conc()
cond()

print('\nContagem Customizada')

i = int(input('Digite o valor de inicio da contagem: '))
f = int(input('Digite o valor de fim da contagem: '))
p = int(input('Digite o valor do passo da contagem: '))
m = int(input('Digite a ordem - 0 P/ Crescente ou 1 P/ Decrescente: '))

concusto(i, f, p, m)

"""

#Método Guana

from time import sleep 

def contador(i, f, p):
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)


    if p < 0:
        p *= -1
    if p ==0:
        p = 1

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush = True) #Tira o buffer de tela
            sleep(0.5)
            cont += p
        print('FIM!!!')
    else:
        cont = i
        while cont >=f:
            print(f'{cont}', end = ' ', flush = True)
            sleep(0.5)
            cont -= p
        print('FIM!!!')


#Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!!!')
ini = int(input('Inicio: '))
fin = int(input('Fim: '))
passo =  int(input('Passo: '))

contador(ini, fin, passo)
