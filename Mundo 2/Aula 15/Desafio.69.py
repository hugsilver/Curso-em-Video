

cont1 = 0
cont2 = 0
cont3 = 0
status = 0
id = sex = 0

while True:
    id = int(input('Digite a idade da pessoa: '))

    while True:
        sex = str(input('Digite o sexo da pessoa - [M/F]: ')).upper()
        if sex == 'M' or sex == 'F':
            break

    if(id > 18):
        cont1 += 1
    if(sex == 'M'):
        cont2 += 1
    if(id <20) and (sex == 'F'):
        cont3 += 1


    status = str(input('Deseja continuar ? [S/N]: ')).upper()

    if status not in ('S' , 'N'):
        status = str(input('Deseja continuar ? [S/N]: ')).upper()

    if status == 'N':
        break

print(f'Existem {cont1} pessoas com mais de 18 anos. ')
print(f'Foram cadastrados {cont2} homens.')
print(f'{cont3} mulheres com menos de 20 anos.')




