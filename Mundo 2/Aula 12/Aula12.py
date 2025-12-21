#
#
nome = str(input('Qual é o seu nome: '))
if nome == 'Hugo':
    print('Gostoso')

elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem comum no Brasil.')
elif nome in 'Ana Cláudia Jessica Juliana':
    print('Belo nome, moça.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}'.format(nome))

