

#help() #Função interna de ajuda


#print('Olá. mundo!!')

#help(input)

#print(input.__doc__) - Outro método


#DOCSTRINGS - STRING DE DOCUMENTAÇÃO


#Exemplo


def contador(i, f, p): #Parametros reais #Usar docs Strinf - Usar duas aspas duplas logo após o inicio do def ''' ''' - COMEÇAR A USAR  
    '''
    Docstring para contador
    
    :param i: Inicio da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    '''
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!!!')

#contador(0, 100, 10) #Parametros formais - Copia dos parametros formais para os reais

#help(contador)


#PARAMETROS OPCIONAIS       



def somar(a=0, b=0, c=0): #Se por acaso não receber c, se torna 0 - Parametro opcional - Podendo colocar todos
    '''
    Docstring para somar
    -> Faz a soma de três valores e mostra o resultado na tela
    :param a: Primeiro valor
    :param b: Segundo valor
    :param c: Terceiro valor
    '''
    soma = a +b + c
    print(f'A soma vale {soma}', end=' ') #end opcional

somar(3, 2, 5)
somar(8, 4) # Vai da erro , se nãor tiver o opcional
somar()
#somar(3, 3, 5, 8) #utilizar muitos parametros

somar(b=4, c=2)

#Escopo de váriavies - Onde a váriavel vai ou não existir

'''
def teste():
    x = 8 
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


#Programa Principal
n = 2 #Variavel global 

print(f'No programa princial, n vale {n}')
teste()
print(f'No programa princial, x vale {x}') # X tem escopo local

#Tudo declarada dentro de uma def vira local
'''

'''
def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
funcao()
print(f'N1 fora vale {n1}')
'''


def somar(a=0, b=0, c=0): #Se por acaso não receber c, se torna 0 - Parametro opcional - Podendo colocar todos
    soma = a +b + c
    return soma


r1 =  somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)

#Ou
print(somar(3, 2, 5))

print(f'Meus cálculos deram {r1}, {r2} e  {r3}')