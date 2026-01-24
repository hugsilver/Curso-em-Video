
def pyhelp(fun):

    modtex2(fun)
    return fun

def modtex(a):
    b = ('~'*(len(a)))
    print(f"\033[37;42m{b}\033[0m")
    print(f"\033[37;42m{a}\033[0m")
    print(f"\033[37;42m{b}\033[0m")

def modtex2(fun):

    c = ('~'*(30 + len(fun)))
    d = (f'Acessando o manual do comando {fun}')
    print(f"\033[37;44m{c}\033[0m")
    print(f"\033[37;44m{d}\033[0m")
    print(f"\033[37;44m{c}\033[0m")
    #e = str(help(fun))
    print(f"\033[30;47m\033[1m")
    print(f"\033[30;47m{help(fun)}\033[0m")


modtex('SISTEMA DE AJUDA PyHELP')

fun = pyhelp(str(input('Função ou Biblioteca >')))

#Falta colcoar em laço de repetição While = True p/ varias funções ou bibliotecas e voltar pro menu (Pro painel), quando digitar o fim, dar mensagem e finalizar
