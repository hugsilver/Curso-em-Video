

list1 = []
listp = []
listi = []
status = 0

#Podendo declarar como list - Exemplo - pares = list()

while True:
    list1.append(int(input('Digite valores para adicionar a lista: ')))

    status = str(input('Deseja continuar - [S/N] ? ')).upper()[0]

    if 'S' in status:
        print()
    elif 'N' in status:
        break

for n in list1:
    if n % 2 == 0:
        listp.append(n)
    elif n % 2 != 0:
        listi.append(n)

print(f'A lista original é: {list1}')
print(f'A lista apenas com os pares: {listp}')
print(f'A lista apenas com os impares: {listi}')
