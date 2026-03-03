
#Falta: Salvar dados no arquivo
#OBS: Varificar como escrever e ler, se possivel VSV - Valores separados por virgula
#Falta: Apresentar dados do arquivo

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
        while True:
            id = input(f'Digite a idade do(a) cliente {name}: ')
            c,t = valida_id(id) #c recebe o retorno da função valida_id do parametro de valor
            #t = valida_id(id) #t recebe o retorno da função valida_id do parametro status
            if t == True: # Se  t receber o status de verdadeiro - Siginifica que a variavel foi validada como inteiro
                break #Nesse caso aceita o valor e finaliza a entrada
        cadastro(name, c) #Chamando a função de cadastro
    elif select == 3:
        os.system("cls") 
        print('\nDados salvos!!!')
        print('Obrigado por usar noss sistema.')
        break
    else:
        os.system("cls") 
        print('\nDigite uma opção valida!!!')
        
    































