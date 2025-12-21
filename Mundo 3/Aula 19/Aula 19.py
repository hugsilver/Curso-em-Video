
'''
pessoas = {'nome': 'Hugo', 'sexo': 'Masculino', 'idade': '32'}
print(pessoas)
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') #Usar aspas duplas, pois já esta dentro da aspa simples ''

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())


#Acessar chaves, valores e itens por laços
for k, v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5

print(pessoas)
'''

'''
#Criar um dicionário dentro de uma lista
brasil = []
estado1 = {'uf' : 'Rio de Janeiro' , 'sigla' : 'RJ'}
estado2 = {'uf' : 'São Paulo' , 'sigla' : 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
'''


estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federatica: '))
    estado['sigla'] = str(input('Sigla do Esatdo: '))
    brasil.append(estado.copy()) #Método de copar o conteudo
    #brasil.append(estado[:]) #Não da para fazer fateamento em dicionario
#print(brasil)

for e in brasil:
    for v in e.values():
        print(v)


