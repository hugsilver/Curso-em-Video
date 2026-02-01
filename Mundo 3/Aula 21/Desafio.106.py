'''
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


#Falta validar para que a ultima função ou biblioteca seja limpa, se der enter ele puxa a ultima
'''

#Metodo Guana

#lista de forma global
from time import sleep

c = ('\033[n', '\033[0;30;41m', '\033[0;30;42m', '\033[0;30;43m', '\033[0;30;44m', '\033[0;30;45m', '\033[7;30m');

def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'',4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('^'*tam)
    print(f'  {msg}')
    print('^'*tam)
    print(c[0], end='')
    sleep(1)


#Programa Principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca >'))

    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
    
título('ATÉ LOGO', 1)












