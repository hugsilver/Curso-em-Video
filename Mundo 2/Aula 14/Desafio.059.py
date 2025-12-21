
cond = 0

x = int(input('Digite o 1° número: '))
y = int(input('Digite o 2° número: '))

while (cond != 5):

    print('\n[1] - Somar \n[2] - Multiplicar \n[3] - Maior \n[4] - Novos números \n[5] - Sair do Programa \n')
    cond = int(input('Digite a operação desejada: '))

    if cond == 1:
        print('A soma é {}'.format(x+y))
    elif cond == 2:
        print('A multiplicação é {}'.format(x*y))
    elif cond == 3:
        print('O maior entre {} e {} é {}'.format(x, y, max(x , y)))
    elif cond == 4:
        x = int(input('Digite um novo valor para X: '))
        y = int(input('Digite um novo valor para Y: '))
    elif cond == 5:
        print('')
    elif cond > 5:
        print('Operação invalida!!!')

print('Programa finalizado!')







