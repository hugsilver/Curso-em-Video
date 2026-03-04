'''
def leiaInt():
    while True:
        try:
            a = int(input('Digite um número inteiro: '))
            return a
        except (KeyboardInterrupt, ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro valido.\033[m')

def leiaFloat():
    while True:
        try:
            b = float(input('Digite um número real: '))
            return b
        except (KeyboardInterrupt, ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real valido.\033[m')

j = leiaInt()
f = leiaFloat()

print(f'Você acabou de digitar os números - Inteiro: {j} e o Real: {f}')
'''

#Método Guana

def leiaInt(msg):
    while True:
        try:#OBS: O tratamento de execssão não pode fazer o programa parar
            a = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro valido.\033[m')
            continue #Laço - Continue joga novamente para o laço
        except (KeyboardInterrupt): #Aceita mais de um except
            print('\nUsuário oreferiu não digitar esse número.')
            return 0
        else: #Se tudo der certo
            return a

def leiaFloat(msg):
    while True:
        try:
            b = float(input(msg))
        except (KeyboardInterrupt, ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return b


j = leiaInt('Digite um Inteiro: ')
f = leiaFloat('Digite um Real: ')

print(f'Você acabou de digitar os números - Inteiro: {j} e o Real: {f}')

