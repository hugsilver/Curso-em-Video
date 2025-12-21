

'''
db_alunos = {'nome': 0, 'nota1': 0, 'nota2': 0, 'media': 0, 'situ': 0}

db_alunos['nome'] = str(input('Digite o nome do aluno: '))
db_alunos['nota1'] = float(input('Digite a 1° nota: '))
db_alunos['nota2'] = float(input('Digite a 2° nota: '))
db_alunos['media'] = (db_alunos['nota1'] + db_alunos['nota2'])/2

if db_alunos['media']>=7:
    db_alunos['situ'] = 'Aprovado'
else:
    db_alunos['situ'] = 'Reprovado'

print(db_alunos)

print(f'Nome do aluno: {db_alunos['nome']}, sua média é: {db_alunos['media']}, logo está {db_alunos['situ']}')

'''



#Método Guana

aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Medida de {aluno["nome"]}: '))

if aluno['media']>=7:
    aluno['situ'] = 'Aprovado'
elif 5 <= aluno['media']<7:
    aluno['situ'] = 'Recuperação'
else:
    aluno['situ'] = 'Reprovado'

#print(aluno)

print('-='*30)
for k, v in aluno.items():
    print(f' - {k} é igual a  {v}')
