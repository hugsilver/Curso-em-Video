#Não consegui
#Falta validar só está indo uma entrada
#Ver resolução do Guana

def leiaInt(n):

    valido = False
    
    try:
        a = int(n)
    except (KeyboardInterrupt, ValueError):
        print('\033[0;31mERRO! Digite um número inteiro valido.\033[m')
        return 0
    else:
        return n

def leiaFloat(r):
    try:
        b = float(r)
    except (KeyboardInterrupt, ValueError):
        print('\033[0;31mERRO! Digite um número real valido.\033[m')
        return 0
    else:
        return r

n = leiaInt(input('Digite um número inteiro: '))
r = leiaFloat(input('Digite um número real: '))

print(f'Você acabou de digitar os números - Inteiro: {n} e o Real: {r}')