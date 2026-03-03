
#Criar arquivo de texto caso não exista
#Cadastrar pessoas - Nome e idade - Validar idade como inteiro
#Permitir a consulta. 3 opções: 1 - Ver pessoas cadastradas (), 2 - Cadastrar nova Pessoa e 3 - Sair do Sistema
#Quando finalizar um cadastro, voltar pro menu inicial
#Não perder dados - Salvar em arquivo de texto simples
#Caso não exista dados na 1° Consulta, dar mensagem que não existe dados cadastrados
#Criar dois módulos: Cadastro e Consulta

#Iniciar por criar um arquivo de texto e validar se ele ja existe

from mod_arquiv_115 import cv_arq
from mod_cad_115 import cadastro, valida_id
import os

#Programa Principal



while True:
    
    print('\n1 - Ver base cadastrada \n2 - Cadastrar nova pessoa \n3 - Sair do sistema')
    select = input('\nDigite a opção desejada: ')
    try:
        a = int(select)
    except (KeyboardInterrupt, ValueError):
        print('\nDigite uma opção valida!!!')
    else:
        select = int(select)
    if select == 1:
        if __name__ == "__main__":
            cv_arq(base_dir=__file__)   
    elif select == 2:
        name = input('Digite o nome do cliente(a): ')
        id = input(f'Digite a idade do(a) cliente {name}: ')
        c = valida_id(id)
        cadastro(name, c)
    elif select == 3:
        os.system("cls") 
        print('\nDados salvos!!!')
        print('Obrigado por usar noss sistema.')
        break
    else:
        os.system("cls") 
        print('\nDigite uma opção valida!!!')
        
    































