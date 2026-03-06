from Desafio115metGuana.lib.interface import * #Import * - Importa tuo
from time import sleep

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabeçalho('Opção 2')
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do Sistema... Até logo!!!')
        break
    else:
        print('ERRO! Digite uma opção váida!') #Não coloquei a cor nessa porra
    sleep(2)















