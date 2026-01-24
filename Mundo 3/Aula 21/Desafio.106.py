
def pyhelp(fun):

    modtex2(fun)
    return fun

def modtex(a): #Função para colorir o 1° Texto
    b = ('~'*(len(a)))
    print(f"\033[37;42m{b}\033[0m")
    print(f"\033[37;42m{a}\033[0m")
    print(f"\033[37;42m{b}\033[0m")

def modtex2(fun): #Função para colorir o Texto da função
    c = ('~'*(30 + len(fun)))
    d = (f'Acessando o manual do comando {fun}')
    print(f"\033[37;44m{c}\033[0m")
    print(f"\033[37;44m{d}\033[0m")
    print(f"\033[37;44m{c}\033[0m")
    #e = str(help(fun))
    print(f"\033[30;47m\033[1m")
    fun = print(f"\033[30;47m{help(fun)}\033[0m")
    return fun


while True:

    x = 0
    modtex('SISTEMA DE AJUDA PyHELP')
    x = str(input('Função ou Biblioteca >'))
    if x == 'EXIT':
        break

    fun = pyhelp(x)
    print(f"\033[30;47m\033[1m")
    print(fun)


#Falta retornar pro menu principal