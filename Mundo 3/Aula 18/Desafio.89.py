
'''
import statistics

listalnota = [[], [[]]]
listp = list()
listm = list()# Deça forma basta eu adicionar essa lista dentro de outra, que não irei precisar de outra metodologia
name = 0
nota1 = nota2 = medi = 0
status = 0
status2 = 0
i = 0
while True:
    name = str(input('Digite o nome do Aluno: '))
    listalnota[0].append(name)
    #Contar alunos existes para criar mais espaço na lista
    #print(len(listalnota[0]))
    if len(listalnota[0]) >= 2:
        listalnota[1].append([]) #Criou, deu certo, mas agora tem que adicionar na nova criada
    #Ainda esta sobreponto e repetido em toda a lista já criada
    #print(listalnota)
    nota1 = float(input('Digite a primeira nota: '))
    listp.append(nota1)
    nota2 =  float(input('Digite a segunda nota: '))
    listp.append(nota2)
    #print(listp)
    listalnota[1][i] = listp[:] #Rcebe um copia da lista provisoria
    #print(listalnota)
    listp.clear() #Limpa a lista provisoria
    i += 1
    #print(listp)

    status = str(input('Deseja continuar? [S/N]: ')).upper()[0]

    if status == 'N':
        break

#print(listp)
#print(listalnota)
#print(listalnota[1][0])

for j in range(0, len(listalnota[0])):
    listm.append(statistics.mean(listalnota[1][j]))

#print(listm)

#print(len(listalnota[0]))

print('=-'*30)
print('No','Nome'.center(20),'Média')
print('-'*60)

for x in range(0, len(listalnota[0])):
    print(x,'',listalnota[0][x].center(21),listm[x])

while True:
    status2 = int(input('Mostrar notas de qual aluno? (999 - Para interromper ): '))

    if status2 <len(listalnota[0]):
        print(f'As notas de {listalnota[0][status2]} são: {listalnota[1][status2]}')

    elif (status2 >= len(listalnota[0])) and status2 != 999: #Só falta isso par ada certo
        print('Aluno não estã na lista')

    elif status2 == 999:
        break
'''
from http.client import responses

#Método Guana

ficha = list()

while True:
    nome = str(input('Digite o nome do aluno:  '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    responses = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if responses == 'N':
        break

print('-'*30)
print(f'{'No.':<4} {'NOME':<10} {'MÉDIA':>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8.1f}')

while True:
    print('-'*35)
    opc =  int(input('Mostrar notas de qual aluno? (999 - Interrompe): '))

    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha):
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')


print('VOLTE SEMPRE')







