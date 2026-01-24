def leiaint(n):

    #print(type(n))
    i = 0
    try:
        int(n)
        i = 1
        return n,i
    except ValueError:
        print('DIGITE UM NÚMERO INTEIRO.')
        i = 0
        return n, i
        #return False

'''
    if type(n) == int:
        return n
    else:
        print('DIGITE UM NÚMERO INTEIRO.')
'''

#Programa Principal
valor = input('Digite um valor inteiro: ')
n = leiaint(valor)

#print(n[1])

if n[1] == 1:
    print(f'Você acabou de digitar o número {n[0]}')

