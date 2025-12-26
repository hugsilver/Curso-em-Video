
from time import sleep 

i = f = p = m = 0

def conc():
    print('Contagem Crescente:')
    
    for j in range(0,11):
        print(j, end=' ')
        sleep(0.1)
        
def cond():
    print('\nContagem Decrescente:')
    for j in range(10, 0, -2):
        print(j, end=' ')
        sleep(0.1)

conc()
cond()

print('\nContagem Customizada')

i = int(input('Digite o valor de inicio da contagem: '))
f = int(input('Digite o valor de fim da contagem: '))
p = int(input('Digite o valor do passo da contagem: '))
m = int(input('Digite a ordem - 0 P/ Crescente ou 1 P/ Decrescente'))







