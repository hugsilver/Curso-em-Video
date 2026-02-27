def metade(p, f=1):
    
    if f == True:
        return format(p/2)
    else:
        return p/2

def dobro(p, f):
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
