def metade(p, f=1):
    
    if f == True:
        return format(p/2)
        #Interessante usar uma variavel local para receber o calculo , retornar somente ela
    else:
        return p/2

def dobro(p, f=0):
    if f == True:
        return format(p*2)
    else:
        return p*2

def aumentar(p, per, f):
    if f == True:
        return format(p*(1+per))
    else:
        return p*(1+per)

def diminuir(p, valor, f):
    if f == True:
        return format(p - valor)
    else:
        return (p - valor)

def format(tex):
    x = str(tex)
    texf = 'R$' + x 
    return texf


def resume(a, b,c):
    print('-'*40)
    print('RESUMO DO VALOR'.center(40))
    print('-'*40)
    ntex = format(a)
    print('PREÇO ANALISADO: ', end='')
    v = len(str(a))
    print(ntex.rjust(27-v))
    print('DOBRO DO PREÇO: ', end='')
    l = len(str(dobro(a)))
    ntex2 = format(dobro(a))
    print(ntex2.rjust(29-l))
    print(f'{b}% de aumento: ', end='')
    t = round(a*(1+b/100), 2) #Formatando com duas casas decimais
    nvalor = format(t) 
    j = len(str(nvalor))
    print(nvalor.rjust(30-j))
    print(f'{c}% de redução: ', end='')
    r = round(a*(1-c/100), 2) #Formatando com duas casas decimais
    nvalorr = format(r)
    m = len(str(nvalorr))
    print(nvalorr.rjust(30-m))








