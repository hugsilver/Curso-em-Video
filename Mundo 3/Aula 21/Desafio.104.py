def leiaint(n):

    n = int(n)
    print(type(n))

    if type(n) == int:
        return n
    else:
        print('DIGITE UM NÚMERO INTEIRO.')

#Programa Principal
valor = input('Digite um valor inteiro: ')
n = leiaint(valor)
print(f'Você acabou de digitar o número {n}')

#Ver resolução dessa
