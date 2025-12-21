
lista_num = []
status = 0

while True:
    valor = int(input('Digite um valor: '))

    if valor in lista_num:
        print('Valor existente, não será adicionado!!!')

    elif valor not in lista_num:
        lista_num.append(valor)
        print('Valor adicionado com sucesso!')

    status = str(input('Deseja continuar? [S/N]: ')).upper()

    if 'S' in status:
        status = 0
    elif 'N' in status:
        break

print(f'Os valores digitados foram: {sorted(lista_num)}')

