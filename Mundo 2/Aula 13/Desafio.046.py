

from time import sleep

for i in range(10, -1, -1): # Laço de repetição iniciando em 10 até -1, sendo que vai até 1, com incremento de -1
#Final do range, o ultimo termo é sempre ignorado.
    print('Contagem: {} segundos'.format(i))
    sleep(0.5)
print('Fogos')
