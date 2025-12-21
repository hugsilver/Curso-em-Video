
termoum = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

an = 0

for i in range(1, 11, 1):
    an = termoum + (i-1)*razao
    print(an, end=' -> ')

print('ACABOU')
#print('Os dez primeiros termos dessa PA, são: {}'.format(PA))

