
'''
dic_base = {'nome': 0,'sexo': 0, 'idade': 0 }
lista_dic = list()
lista_temp = list()
dicionario = dict()
i = 0
soma = 0

while True:
    i += 1
    name = str(input('Digite o nome da pessoa: '))
    dic_base['nome'] = name
    sex = str(input('Digite o sexo da pessoa - M/F: ').upper().strip()[0])
    dic_base['sexo'] = sex
    idad = int(input('Digite a idade da pessoa: '))
    dic_base['idade'] = idad
    lista_temp = dic_base.copy()
    lista_dic.append(lista_temp)
    statistics = str(input('Deseja continuar? [S]/[N]: ').upper())

    if statistics == 'N':
        break

#print(lista_dic)

print(f'Foram cadastradas {i} pessoas.')

for k in range(0, i):
    soma = soma + lista_dic[k]['idade']

print(f'A média de idade do grupo é {soma/i} anos.')

print('Lista apenas com as mulheres do grupo: ')

for j in range(0, i):
    if lista_dic[j]['sexo'] == 'F':
        print(lista_dic[j]['nome'])

print('Lista apenas com pessoas com idade acima da média do grupo: ')
for l in range(0, i):
    if lista_dic[l]['idade'] > soma/i:
        print(f'Nome: {lista_dic[l]['nome']}, sexo {lista_dic[l]['sexo']} e idade de {lista_dic[l]['idade']} anos')
'''

#Metodo Guana
galera = list()
pessoa = dict()

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Digite o nome da pessoa: '))
    while True:
        pessoa['sexo'] = str(input('Digite o sexo da pessoa - [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Digite apenas M ou F.')
    pessoa['idade']=int(input('Digite a idade da pessoa: '))
    galera.append(pessoa.copy())
    while True:
        resp =  str(input('Deseja continuar? [S]/[N]: ').upper()[0])
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print('-='*30)
print(pessoa)
