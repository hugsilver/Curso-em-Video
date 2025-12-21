
import random

print('\n1 - Para PEDRA \n2 - Para PAPEL \n3 - Para TESOURA')

a = int(input('Digite:'))

computer = random.randint(1,3)

if a == 1 and computer == 3:
    print('Você ganhou, PEDRA ganha de TESOURA. ')
elif a == 2 and computer == 1:
    print('Você ganhou, PAPEL ganha de PEDRA.')
elif a == 3 and computer == 2:
    print('Você ganhou, TESOURA ganha de PAPEL.')
elif a == computer:
    print('Deu empate, tente novamente.')
else:
    print('A máquina ganhou, começe a se preparar.')


