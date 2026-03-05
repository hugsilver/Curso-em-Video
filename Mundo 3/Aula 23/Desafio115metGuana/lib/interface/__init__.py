
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

def linha(tamanho = 42):
    return '-'*tamanho

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc



    








