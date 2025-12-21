

person = list()
personp = list()
just_p = list()
maxi =  mini = 0

status = quant_leve = quant_pes = ind = 0

while True:
    person.append(str(input('Digite o nome da pessoa: ')))
    person.append(float(input(f'Digite o peso da pessoa em Kg: ')))
    personp.append(person[:]) #Copia, fatiamento completo
    person.clear()#Se não tiver esse clear ela vai adicionar sobreposto, ou seja, na proxima vez que os inputs forem adicionado a lista ficara maior
    # [inicial], [inicial + proximo], [inicial + proximo + outro] - Por isso tem que apagar a lista

    ind += 1

    status = str(input('Deseja cadastrar mais pessoas - [S/N]: ')).upper()[0]

    if 'N' in status:

        break


print(f'Foram cadastradas {ind} pessoas. ')
#print(personp)

for p in personp:
    just_p.append(p[1])

#print(just_p)
maxi = max(just_p)
mini = min(just_p)

print(f'O maior peso foi {maxi}')
print('Peso de', end=' ')
for j in personp:
    if j[1] == maxi:
        print({j[0]}, end=' ')


print(f'\nO menor peso foi {mini}')

print('Peso de', end=' ')
for i in personp:
    if i[1] == mini:
        print({i[0]}, end=' ')



