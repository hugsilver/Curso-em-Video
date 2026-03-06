from Desafio115metGuana.lib.interface import * #Import * - Importa tudo
from Desafio115metGuana.lib.arquivo import *
from time import sleep

arq = r'C:\Users\u1012290\Documents\GitHub\Curso-em-Video\Mundo 3\Aula 23\cursoemvideo.txt'
#Não se p1 não funcinou pelo script do Guana

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        #Opção de cadastar nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do Sistema... Até logo!!!')
        break
    else:
        print('ERRO! Digite uma opção váida!') #Não coloquei a cor nessa porra
    sleep(2)















