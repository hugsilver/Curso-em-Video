cont = 0
print('Jogo PAR ou ÍMPAR.')


import random

while True:
     value = esc = soma = maq = pivo = 0

     value = int(input('Diga um valor: '))
     esc = str(input('Par ou Impar? [P/I]:').upper())
     maq =+ random.randint(1,10)
     soma = value + maq
     print(f'Você escolheu {value} e a maquina escolheu {maq} sendo o resultado {soma}')
     if soma % 2 == 0:
        pivo = 'P'
        print('Resultado PAR')
     else:
         pivo = 'I'
         print('Resultado IMPAR')

     if pivo == esc:
        cont += 1
        print('GANHOU')
     else:
        break

print(f'Você perdeu, conseguiu ganhar {cont} vezes')






