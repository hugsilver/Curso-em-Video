
def fatorial(num=1, show = 0):
    '''
    Docstring para fatorial
    -> Calcular o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    : return: O valor do Fatorial de um núemro n
    '''
    f = 1

    if show == False:
        for c in range(num, 0, -1):
            f *= c  
        return f
    
    elif show == True:
        for c in range(num, 0, -1):
            f *= c
            print(c, end='')
            print(' X ', end='')
        print('=',end=' ')
        #print(f)
        return f
        

print(fatorial(5, show = False))







