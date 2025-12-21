#Part.1
'''
teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()

galera.append(teste[:]) #Copia
teste[0] = 'Maria'
teste[1] = 22

galera.append(teste[:]) #Copia
print(galera)
'''


#Part.2
'''
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
#print(galera[3][1]) #Estrutura de dados

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
'''


#Part.3


galera = list()
dado = list()
totmai = totmen = 0

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # Lista dentro de lista - Com copia
    dado.clear() #Limpar

print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')

