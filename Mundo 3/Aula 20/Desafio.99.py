'''
def max_find(*listas):
    maximo = max(listas)
    print('-='*30)
    print('Analisando os valores passados!!!')
    print(listas)
    print(f'Foram análisados {len(listas)} valores ao todo.')
    print(f'O maior valor informado foi {maximo}')
    

max_find(2, 9, 4, 5, 7, 1)
max_find(4, 7, 0)
max_find(1, 2)
max_find(6)
#max_find() - Não consegui o ultimo
'''


#Metodo Guana

from time import sleep

def maior(* num): # *Desempacotar
    cont = maior = 0
    print('-='*20)


    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor}', end= ' ', flush = True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont =+ 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
            

#Programa principal

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()


