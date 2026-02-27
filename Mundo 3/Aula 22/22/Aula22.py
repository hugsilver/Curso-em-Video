#import uteis 

from uteis import numeros
#Usar essa

#from uteis import fatorial, dobro - Método não recomendavel pelo Pyhton
#Pode ter comflitos em entre funções

#Programa Principal
num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro da váriavel {num} é {numeros.dobro(num)}')

# Nome da biblioteca.função - Exemplo uteis22.dobro(X) - X argumento 
#Pacotes - Separação por assuntos - Que tem várias funções com varios módulos 



