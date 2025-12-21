'''
cont = 1
while True: #Executou em loop infinito
    print(cont, '-> ', end='')
    cont += 1

print('Acabou')
'''
#Pyhton não declara variavel, mas sim inicializa

n = s = 0

'''
while n != 999: # n != 999Flag
    n = int(input('Digite um número: '))
    s += n
s -= 999
print('A soma vale {}'.format(s))
'''

'''
while True: # n != 999Flag
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n

#print('A soma vale {}'.format(s))

print(f'A soma vale {s}') # f string
'''

nome = 'José'
idade = 33
salário = 987.55

print(f'O {nome} tem {idade} anos e ganha R$ {salário:.2f}.')
#print('O {} tem {} anos.'.format(nome , idade))


