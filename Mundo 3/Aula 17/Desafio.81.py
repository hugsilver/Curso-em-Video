

list = []

while True:

    list.append(int(input('Digite um valor a ser adicionado na lista: ')))
    status = str(input('Você deseja continuar - [S/N]:')).upper().strip()[0]

    '''
    if 'S' in status:
        print()
        #list.append(int(input('Digite um valor a ser adicionado na lista: ')))
        #status = str(input('Você deseja continuar - [S/N]:')).upper().strip()[0]
    '''
    if 'N' in status:
        break

print(list)

print(f'Foram digitados: {len(list)}')
print(f'Os valores ordenados em foram decrescente: {sorted(list, reverse=True)}')
if 5 in list:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')
