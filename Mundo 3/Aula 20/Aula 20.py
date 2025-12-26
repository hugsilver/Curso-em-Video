
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


def contador(*num): # * - Simbolo de desempacotar, quantos vierem nos parametros
    print(num) #Criou tupla

contador(5, 7, 3, 1, 4)
contador(8, 4, 7)
contador(4, 4, 7, 6, 2)

#Empacotamento - Empacotar



