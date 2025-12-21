


termoum = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

an = 0
c = 0
cond = 0
ajust = 0



while (cond != 3):
    print('\n[1] - Apresentar os 10° primeiros termos\n[2] - Apresentar mais termos \n[3] - Parar programas\n')
    cond = int(input('Digite a operação desejada: '))
    if cond == 1:
        c = 0
        ajust = 0
        while (c < (11 + ajust)):
            an = termoum + (c - 1) * razao
            print(an, end=' -> ')
            c += 1
    elif cond == 2:
        c = 0
        ajust = int(input('Digite quantos termos a mais deseja apresentar: '))
        while (c < (11 + ajust)):
            an = termoum + (c - 1) * razao
            print(an, end=' -> ')
            c += 1
    elif cond > 3 or cond == 0:
        print('Operação invalida!!!')
    print(cond)

print('ACABOU')
#print('Os dez primeiros termos dessa PA, são: {}'.format(PA))
