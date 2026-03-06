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
        print(a.read()) #readlines - Pega as linhas e joga dentro de uma lista 

    
