from datetime import date

id = 0
status = 0

def valida_id(id):
    '''
    Docstring para valida_id
    
    :param id: Recebe a idade da pessoa

    '''
    if id >=18 and id < 70:
        status = 'OBRIGATORIO'
        return status 
    elif id >= 16 and id < 18:
        status = 'FACULTATIVO' 
        return status 
    elif id > 70:
        status = 'FACULTATIVO'
        return status 
    else:
        status = 'NEGADO'
        return status 
    


year_nascimento = int(input('Digite o ano em que você nasceu: '))
hoje = date.today()
id = hoje.year - year_nascimento
result = valida_id(id)

print(f'Para idade de {id} o voto é {result}')




