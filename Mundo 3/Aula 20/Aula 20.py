
'''
def lin():
    print('-'*30)


#PROGRAMA PRINCIPAL
#print('-'*30)
lin()
print('CURSO EM VÍDEO')
lin()
lin()
#print('-'*30)
#print('-'*30)
print('APRENDA PYTHON')
lin()
lin()
#print('-'*30)
#print('-'*30)
print('HUGO SILVA')
lin()
#print('-'*30)
'''


'''
def titulo(txt): #txt é o nome do argumento
    print('-'*30)
    print(txt) #Passando o argumento
    print('-' * 30)

#PROGRAMA PRINCIPAL
titulo('CURSO EM VÍDEO') #Argumento em verde
titulo('APRENDA PYTHON')
titulo('PYTHON É TOP')
titulo('HUGO SILVA')

'''

'''
a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A = {a} + B = {b} vale {s}')

#Programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(b = 4, a = 1)
soma(7, 2)
'''

#Empacotamento - Empacotar ou Desempacotamento
'''
def contador(*num): # * - Simbolo de desempacotar, quantos vierem nos parametros
    for valor in num:
        print(f'{valor}', end='')
    print('FIM')

def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao total {tam} números.')

contador(5, 7, 3, 1, 4)
contador(8, 4, 7)
contador(4, 4, 7, 6, 2)
'''


#Dobrando valores de uma lista

'''
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]

dobra(valores)
print(valores)
'''

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s} ')

soma(5, 2)
soma(2, 9, 4)




