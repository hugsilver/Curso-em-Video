

products = [ ]
values = []
cont1 = 0
sum = 0
status = 0

while True:

    products.append(str(input('Digite o nome do produto: ')))
    valor = float(input('Digite o valor do produto: '))
    values.append(valor)

    sum += valor

    if valor > 1000:
        cont1 += 1


    status = str(input('Deseja continuar - [S/N]: ')).upper()

    if status not in ('S' , 'N'):
        status = str(input('Deseja continuar ? [S/N]: ')).upper()

    if status == 'N':
        break

indice_menor = values.index(min(values)) #Pedi pro chat me ensinar uma técnica
#Dessa forma o indice da minha lista prosucts será o mesmo quando achar o indice da minha lista values


print(f'O total de gastos da compra foi R$ {sum:.2f}')
print(f'Existem {cont1} produtos com valora acima de R$ 1.000,00 ')
print('O produto mais barato é {},'
      ' valor: R$ {}'.format(products[indice_menor] , min(values)))

