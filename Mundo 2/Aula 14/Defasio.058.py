
import random
import time

print('Estou pensando em um número entre 0 e 10.')
print('Espere....')
for c in range(1, 4):
    print(c)
    time.sleep(0.5)

PCnum =  random.randint(0,10)

print('`Pensei. Tente adivinha o número: ')

miturn = 0
count = 0

while (miturn != PCnum):
       miturn = int(input('Digite o número: '))
       count = count + 1

print('Você acertou miseravel e precisou de {} tentativas.'.format(count))



