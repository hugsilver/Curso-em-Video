'''

from datetime import date

id = 0
status = 0

def valida_id(id):

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
    

#Programa Principal
year_nascimento = int(input('Digite o ano em que você nasceu: '))
hoje = date.today()
id = hoje.year - year_nascimento
result = valida_id(id)

print(f'Para idade de {id} o voto é {result}')
'''

#Metodo Guanabara

def voto(ano):
    from datetime import date #Escopo de importação - Economiza memoria - Se for necessario somente dentro da função
    atual = date.today().year
    idade = atual - ano

    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade <18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGÁTORIO.'


nas = int(input('Em que ano você nasceu? '))
print(voto(nas))


