
termoum = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

an = 0
c = 0

while (c < 11):
    an = termoum + (c-1)*razao
    print(an, end=' -> ')
    c += 1

print('ACABOU')
#print('Os dez primeiros termos dessa PA, são: {}'.format(PA))
