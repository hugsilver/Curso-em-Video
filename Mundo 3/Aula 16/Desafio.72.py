
tup_num_ext = ('zero', 'um' , 'dois', 'três' , 'quatro' , 'cinco' , 'seis' , 'sete' , 'oito' , 'nove' ,
               'dez' , 'onze' , 'doze' , 'treze' , 'quatorze' , 'quinze' , 'dezesseis' , 'dezesete' ,
               'dezoite' , 'dezenove' , 'vinte')

num = status = c = 0

while True:

    num = int(input('Digite um número: '))

    while True:
        if  (0 <= num <= 20) and (c==0):
            print(f'O número digitado é: {tup_num_ext[num]}')
            #print(c)
            c=0
            break

        elif (0 <= num <= 20) and (c>0):
            num = int(input('Digite um número: '))
            print(f'O número digitado é: {tup_num_ext[num]}')
            #print(c)
            c=0
            break
        else:
            print('Tente novamente!')
            num = 0
            c = +1

    status = str(input('Deseja continaur ? [S/N]: ')).strip().upper()[0]
    if status == 'N':
        break









