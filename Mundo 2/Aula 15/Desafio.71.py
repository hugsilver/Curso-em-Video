
sac = restante = int50 = int20 = int10 = int1 = 0
rest = 0


int_notas = [] #Lista para receber os inteiros para cada valor de nota

print('BANCO TIO PATINHA - SUA DÍVIDA É NOSSA FELICIDADE')
print('Notas disponiveis: R$ 50, R$ 20, R$ 10 E R$ 1,00 ')

sac = int(input('Digite o valor que deseja sacar: '))

while True:

    int50 = sac//50 #// Parte inteira da div

    restante = sac - int50*50

    if(restante>0):
        int20 = restante//20
        restante -= int20*20
        if(restante>0):
            int10 = restante//10
            restante -= int10*10
            if(restante>0):
                int1 = restante//1
                restante -= int1*1

    if restante == 0:
        break

print(f'Para o valor de desejado de {sac} reais, recebera: {int50} notas de R$50, {int20} notas de R$20, {int10} notas de R$10 e {int1} notas de R$1,00. ')















