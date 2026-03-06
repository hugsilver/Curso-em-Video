from Desafio115metGuana.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') #rt - Read text
        a.close() #Fechar
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # Criar WT+ - WT:Escerve um arquivo de texto, caso não exista +, o mais cria 
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')    

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
        #print(a.read()) #readlines - Pega as linhas e joga dentro de uma lista
    finally: #Dando certo ou dando errado, finalizar o arquivo
        a.close() 

def cadastrar(arq, nome = 'Desconhecido', idade = 0):
    try:
        a = open(arq, 'at') #AT - append text
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()

