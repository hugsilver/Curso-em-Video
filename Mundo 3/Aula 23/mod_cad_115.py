import os
from mod_arquiv_115 import cv_arq

def cadastro(a = 0, b = 0):
    os.system("cls")
    cv_arq(base_dir=__file__)
    print('Dados cadastrados com sucesso!!!')

def valida_id(idade):
    try:
        b = int(idade)
    except (KeyboardInterrupt, ValueError, TypeError):
        print('\nDigite um valor Inteiro!!!')
    else:
        return int(idade) 

    


